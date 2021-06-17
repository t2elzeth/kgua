from django.test import TestCase

from ..models import User
from ..serializers import UserSerializer
from .mixins import CreateUserAndSuperuserMixin


class TestUserSerializer(CreateUserAndSuperuserMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.users_list = [self.user, self.superuser]

    def test_retrieve_single_user(self):
        """Test serializing single user instance"""
        serializer = UserSerializer(self.user)

        expected_data = {
            "id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
        }

        self.assertEqual(expected_data, serializer.data)

    def test_retrieve_user_list(self):
        """Test serializing multiple user instances"""
        serializer = UserSerializer(self.users_list, many=True)

        expected_data = [
            {
                "id": 1,
                "first_name": self.USER_DATA["first_name"],
                "last_name": self.USER_DATA["last_name"],
                "email": self.USER_DATA["email"],
            },
            {
                "id": 2,
                "first_name": self.SUPERUSER_DATA["first_name"],
                "last_name": self.SUPERUSER_DATA["last_name"],
                "email": self.SUPERUSER_DATA["email"],
            },
        ]

        self.assertEqual(expected_data, serializer.data)

    def test_user_create(self):
        """Test creating new user instance via serializer"""
        request_data = {
            "first_name": "Ulukman",
            "last_name": "Amangeldiev",
            "email": "fullstackdev@gmail.com",
            "password": "adminfullstack",
        }

        serializer = UserSerializer(data=request_data)
        is_valid = serializer.is_valid(raise_exception=True)
        serializer.save()

        expected_data = {
            "id": 3,
            "first_name": request_data["first_name"],
            "last_name": request_data["last_name"],
            "email": request_data["email"],
        }

        self.assertTrue(is_valid)
        self.assertEqual(expected_data, serializer.data)

    def test_user_create_using_existing_data(self):
        """Test user creation using already existing data"""
        serializer = UserSerializer(data=self.USER_DATA)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(User.objects.count(), len(self.users_list))
