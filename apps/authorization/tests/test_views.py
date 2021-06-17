from django.contrib.auth.tokens import default_token_generator
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import SharedAction, Token, User
from ..utils import decode_uid, encode_uid
from .mixins import CreateUserAndSuperuserAndSetCredentialsMixin, UserDataMixin


class TestUserSignUp(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("user-signup")
        self.valid_payload = UserDataMixin.USER_DATA
        self.invalid_payload = {"email": "invalidemail", "password": "invalid password"}

    def test_signup_using_valid_payload(self):
        """Test trying to signup using valid data case"""
        response = self.client.post(self.url, self.valid_payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_using_invalid_payload(self):
        """Test trying to signup using invalid data case"""
        response = self.client.post(self.url, self.invalid_payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_using_empty_payload(self):
        """Test trying to signup using empty data case"""
        response = self.client.post(self.url, {})

        self.assertIn("first_name", response.data)
        self.assertIn("last_name", response.data)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_already_exists(self):
        """Test user already exists case"""
        User.objects.create_user(**self.valid_payload)

        response = self.client.post(self.url, self.valid_payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUserMeEndpoint(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-me")
        self.new_first_name = "My New first name"
        self.new_city = "Bishkek"
        self.new_phone = "996771221103"

    def test_get_me(self):
        """Test getting info about current user case"""
        self.set_credentials()

        response = self.client.get(self.url)

        rdata = response.data
        profile = self.superuser.profile
        self.assertEqual(
            self.superuser.first_name, rdata["first_name"], "First names don't match"
        )
        self.assertEqual(
            self.superuser.last_name, rdata["last_name"], "Last names don't match"
        )
        self.assertEqual(profile.country, rdata["country"], "Countries don't match")
        self.assertEqual(profile.city, rdata["city"], "Cities don't match")
        self.assertEqual(profile.phone, rdata["phone"], "Phones don't match")
        self.assertEqual(profile.picture, rdata["picture"], "Pictures don't match")

    def test_get_me_without_credentials(self):
        """Test trying to get current user info without providing credentials"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_me(self):
        """Test update profile data case"""
        self.set_credentials()

        form_data = {
            "first_name": self.new_first_name,
            "city": self.new_city,
            "phone": self.new_phone,
        }
        response = self.client.patch(self.url, form_data)

        self.superuser.refresh_from_db()
        profile = self.superuser.profile
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.client.get(self.url).data)
        self.assertEqual(self.superuser.first_name, self.new_first_name)
        self.assertEqual(profile.city, self.new_city)
        self.assertEqual(profile.phone, self.new_phone)


class TestUserActivation(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-activation")
        self.uid = encode_uid(self.user.id)
        self.activation_token = default_token_generator.make_token(self.user)

    def test_user_activation(self):
        """Test user email-activation"""
        activation_data = {"uid": self.uid, "token": self.activation_token}
        response = self.client.post(self.url, activation_data)

        self.user.refresh_from_db()
        self.assertEqual(str(self.user.id), decode_uid(self.uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.is_active, "User has not been activated")


class TestUserUpdateEmail(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-update-email")
        self.new_email = "newemail@gmail.com"

    def _get_form_data(self, new_email):
        """Returns form data for request"""
        return {"email": new_email}

    def _make_request(self, form_data):
        """Makes request and returns response"""
        return self.client.patch(self.url, form_data)

    def _update_email(self, new_email):
        self.set_credentials()

        form_data = self._get_form_data(new_email)
        response = self._make_request(form_data)

        self.superuser.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.superuser.email, new_email, "Email was not changed")
        self.assertFalse(
            self.superuser.is_active, "User was not deactivated after email change"
        )
        self.assertFalse(
            Token.objects.filter(user=self.superuser).exists(),
            "User auth-token was not deleted after email change",
        )

    def test_updating_using_new_email(self):
        """Test successfull updating email of the user"""
        # Using superuser, because they are active by default
        self._update_email(self.new_email)

    def test_updating_using_old_email(self):
        """Test updating email of the user using old email"""
        # Using superuser, because they are active by default
        self._update_email(self.superuser.email)

    def test_updating_email_without_auth_token(self):
        """Test updating email without AuthToken"""
        form_data = self._get_form_data(self.new_email)
        response = self._make_request(form_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_updating_email_with_empty_payload(self):
        """Test updating email with empty payload"""
        self.set_credentials()

        form_data = {}
        response = self._make_request(form_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)


class TestUserUpdatePassword(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-update-password")
        self.old_password = self.USER_DATA["password"]
        self.new_password = "new_password"
        self.form_data = {
            "old_password": self.old_password,
            "new_password": self.new_password,
        }

    def test_update_password(self):
        """Test update password case"""
        self.set_credentials()

        response = self.client.patch(self.url, self.form_data)

        self.superuser.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            self.superuser.check_password(self.new_password),
            "User password was not changed",
        )

    def test_update_password_without_credentials(self):
        """Test trying to update password without providing credentials"""
        response = self.client.patch(self.url, self.form_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_password_with_empty_payload(self):
        """Test trying to update password with empty payload"""
        self.set_credentials()

        response = self.client.patch(self.url, {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("old_password", response.data)
        self.assertIn("new_password", response.data)


class TestLogin(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("token-auth-login")
        self.valid_credentials = self.SUPERUSER_DATA
        self.invalid_credentials = {
            "email": "invalidcredentials@gmail.com",
            "password": "invalidcredentialspassword",
        }

    def test_login_with_valid_credentials(self):
        """Test login"""
        response = self.client.post(self.url, self.SUPERUSER_DATA)

        self.assertTrue(Token.objects.filter(user=self.superuser).exists())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(
            "auth_token", response.data, "auth_token is not present in response.data"
        )

    def test_login_with_invalid_credentials(self):
        """Test trying to login using invalid credentials"""
        response = self.client.post(self.url, self.invalid_credentials)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("auth_token", response.data)


class TestLogout(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("token-auth-logout")

    def test_logout(self):
        """Test user logout"""
        self.set_credentials()

        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Token.objects.filter(user=self.superuser).exists(),
            "Token was not deleted after logout",
        )

    def test_logout_without_credentials(self):
        """Test logout without providing auth credentials"""
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestCreateSharedAction(CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("me-shared-actions")
        self.performer_email = self.user.email
        self.action = None

    def _get_form_data(self):
        return {"performer_email": self.performer_email, "action": self.action}

    def _test_create_shared_action(self):
        """Check if creating shared actions is possible"""
        self.set_credentials()

        response = self.client.post(self.url, self._get_form_data())

        shared_action = SharedAction.objects.filter(
            target=self.superuser,
            performer__email=self.performer_email,
            action=self.action,
        ).first()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(shared_action)
        self.assertEqual(shared_action.action, self.action)

    def test_create_update_shared_action(self):
        self.action = SharedAction.ACTION_UPDATE
        self._test_create_shared_action()

    def test_create_ebay_buy_shared_action(self):
        self.action = SharedAction.ACTION_EBAY_BUY
        self._test_create_shared_action()

    def test_create_ebay_sell_shared_action(self):
        self.action = SharedAction.ACTION_EBAY_SELL
        self._test_create_shared_action()

    def test_create_shared_action_for_user_himself(self):
        """Test user creates shared action for himself case"""
        self.set_credentials()

        self.performer_email = self.superuser.email
        self.action = SharedAction.ACTION_UPDATE

        response = self.client.post(self.url, self._get_form_data())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_shared_action_with_no_auth_header_provided(self):
        """Test creating shared action without providing authentication token"""
        self.action = SharedAction.ACTION_UPDATE

        response = self.client.post(self.url, self._get_form_data())

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_shared_action_using_empty_payload(self):
        """Test creating shared action with empty payload"""
        self.set_credentials()

        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUpdateUserWithUpdateSharedAction(
    CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase
):
    def setUp(self):
        super().setUp()
        self.url = reverse("user-detail", kwargs={"pk": self.user.id})
        self.shared_action = SharedAction.objects.create(
            target=self.user,
            performer=self.superuser,
            action=SharedAction.ACTION_UPDATE,
        )
        self.new_first_name = "Test update shared action"
        self.form_data = {"first_name": self.new_first_name}

    def test_with_update_shared_action_provided(self):
        """Check updating user with shared action provided case"""
        self.set_credentials()

        response = self.client.patch(self.url, self.form_data)

        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.first_name, self.new_first_name)

    def test_with_no_update_shared_action_provided(self):
        """Check updating user with no shared action provided case"""
        self.set_credentials()

        self.shared_action.delete()

        response = self.client.patch(self.url, self.form_data)

        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(self.user.first_name, self.new_first_name)

    def test_with_no_auth_header_provided(self):
        """Check updating user with no authentication details provided"""
        response = self.client.patch(self.url, self.form_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestRetrieveSharedActions(
    CreateUserAndSuperuserAndSetCredentialsMixin, APITestCase
):
    def setUp(self):
        super().setUp()
        self.user.activate()
        self.usertoken = Token.objects.create(user=self.user)
        self.target = self.superuser
        self.performer = self.user
        self.shared_actions = [
            SharedAction.objects.create(
                target=self.target,
                performer=self.performer,
                action=SharedAction.ACTION_UPDATE,
            ),
            SharedAction.objects.create(
                target=self.target,
                performer=self.performer,
                action=SharedAction.ACTION_EBAY_SELL,
            ),
            SharedAction.objects.create(
                target=self.target,
                performer=User.objects.create_user(
                    email="userforsharedaction@gmail.com",
                    password="userforsharedaction",
                    first_name="userforsharedaction first name",
                    last_name="userforsharedaction last name",
                ),
                action=SharedAction.ACTION_EBAY_BUY,
            ),
        ]

    def test_get_shared_actions_as_target(self):
        """Test retrieving list of shared actions where current user is target"""
        url = reverse("shared-actions-as-target")

        self.set_credentials()

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), len(self.shared_actions))

    def test_get_shared_actions_as_performer(self):
        """Test retrieving list of shared actions where current user is performer"""
        url = reverse("shared-actions-as-performer")

        self.set_credentials(token=self.usertoken)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)
        for result in response.data:
            self.assertEqual(result["performer_email"], self.performer.email)

    def test_get_shared_actions_with_no_auth_header_provided(self):
        """Test retrieving list of shared actions without providing auth header"""
        as_target_url = reverse("shared-actions-as-target")
        as_performer_url = reverse("shared-actions-as-performer")

        as_target_response = self.client.get(as_target_url)
        as_performer_response = self.client.get(as_performer_url)

        self.assertEqual(as_target_response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            as_performer_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
