from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from . import utils
from .models import User


class SendEmailSerializerMixin:
    def send_email(self, to, context):
        if "view" in self.context:
            self.context["view"].send_email(to, context)


class UserSerializer(SendEmailSerializerMixin, serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]

    def create(self, validated_data: dict):
        """Create user"""
        user = self.Meta.model.objects.create_user(**validated_data)

        self.send_email(user, {"user": user})
        return user

    def update(self, instance, validated_data):
        if "email" in validated_data:
            raise ValidationError({"error": "Email cannot be updated!"})
        return super().update(instance, validated_data)


class MeSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)

        if instance is not None:
            self.instance = instance.profile

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "picture",
            "country",
            "city",
            "phone",
            "locale",
            "is_premium",
        ]

    first_name = serializers.CharField(source="owner.first_name")
    last_name = serializers.CharField(source="owner.last_name")
    email = serializers.EmailField(source="owner.email", read_only=True)

    def update(self, instance, validated_data):
        owner_data = validated_data.pop("owner", {})
        owner = instance.owner
        owner.first_name = owner_data.get("first_name", owner.first_name)
        owner.last_name = owner_data.get("last_name", owner.last_name)
        owner.save()

        return super().update(instance, validated_data)


class ActivationSerializer(SendEmailSerializerMixin, serializers.Serializer):
    uid = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    default_error_messages = {
        "invalid_token": "Invalid token for given user.",
        "invalid_uid": "Invalid user id or user doesn't exist.",
        "stale_token": "Stale token for given user.",
    }

    def validate(self, data):
        self.user = User.objects.get_object_or_none(pk=utils.decode_uid(data["uid"]))

        if self.user is None:
            raise ValidationError({"uid": self.error_messages["invalid_uid"]})
        if self.user.is_active:
            raise PermissionDenied(self.error_messages["stale_token"])

        is_token_valid = default_token_generator.check_token(
            self.user, data.get("token", "")
        )
        if not is_token_valid:
            raise ValidationError({"token": self.error_messages["invalid_token"]})

        return super().validate(data)

    def create(self, validated_data):
        self.user.activate()
        self.send_email(self.user, {"user": self.user})
        return self.user


class ResendActivationEmailSerializer(SendEmailSerializerMixin, serializers.Serializer):
    email = serializers.EmailField()

    default_error_messages = {
        "email_not_found": "User with given email does not exist.",
        "already_active": "User already activated",
    }

    def validate_email(self, email):
        if self._get_user(email) is None:
            return self.fail("already_active")

        return email

    def _get_user(self, email):
        return User.objects.get_object_or_none(email=email, is_active=False)

    def create(self, validated_data):
        user = self._get_user(validated_data["email"])
        self.send_email(user, {"user": user})
        return user


class UpdatePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    default_error_messages = {
        "invalid_credentials": "Unable to log in with provided credentials.",
    }

    def validate(self, data):
        if not self.instance.check_password(data["old_password"]):
            return self.fail("invalid_credentials")

        return super().validate(data)

    def update(self, instance, validated_data):
        old_password = validated_data["old_password"]
        new_password = validated_data["new_password"]

        if old_password != new_password:
            instance.set_password(new_password)
            instance.save()

        return instance


class UpdateEmailSerializer(SendEmailSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.deactivate()

        self.send_email(user, {"user": user})
        return user


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    auth_token = serializers.CharField(source="key", read_only=True)

    default_error_messages = {
        "invalid_credentials": "Unable to log in with provided credentials.",
        "inactive_account": "User account is disabled.",
    }

    def validate(self, data):
        password = data.get("password")
        params = {"email": data.get("email")}
        self.user = authenticate(
            request=self.context.get("request"), password=password, **params
        )
        if not self.user:
            self.user = User.objects.get_object_or_none(**params)
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            return data
        self.fail("invalid_credentials")

    def create(self, validated_data):
        return self.user.login()


# class GoogleAuthSerializer(serializers.Serializer):
#     code = serializers.CharField(required=True)
#
#     def validate(self, attrs):
#         validated_data = super().validate(attrs)
#
#         client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
#         self.id_info = id_token.verify_oauth2_token(
#             self.initial_data["code"], requests.Request(), client_id
#         )
#
#         if self.id_info["iss"] not in [
#             "accounts.google.com",
#             "https://accounts.google.com",
#         ]:
#             raise ValidationError("Wrong issuer.")
#
#         return validated_data
