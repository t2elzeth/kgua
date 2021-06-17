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
            "email": self.user.email,
        }

        self.assertEqual(expected_data, serializer.data)

    def test_retrieve_user_list(self):
        """Test serializing multiple user instances"""
        serializer = UserSerializer(self.users_list, many=True)

        expected_data = [
            {
                "id": 1,
                "email": self.USER_DATA["email"],
            },
            {
                "id": 2,
                "email": self.SUPERUSER_DATA["email"],
            },
        ]

        self.assertEqual(expected_data, serializer.data)

    def test_user_create(self):
        """Test creating new user instance via serializer"""
        request_data = {
            "email": "fullstackdev@gmail.com",
            "password": "adminfullstack",
        }

        serializer = UserSerializer(data=request_data)
        is_valid = serializer.is_valid(raise_exception=True)
        serializer.save()

        expected_data = {
            "id": 3,
            "email": request_data["email"],
        }

        self.assertTrue(is_valid)
        self.assertEqual(expected_data, serializer.data)

    def test_user_create_using_existing_data(self):
        """Test user creation using already existing data"""
        serializer = UserSerializer(data=self.USER_DATA)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(User.objects.count(), len(self.users_list))
