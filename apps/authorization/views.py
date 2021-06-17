from secrets import token_urlsafe

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .email import ActivationEmail, ConfirmationEmail, GoogleAuthNewUserCreated
from .mixins import SendEmailMixin
from .models import User
from .serializers import (ActivationSerializer,
                          MeSerializer, ResendActivationEmailSerializer,
                          TokenSerializer,
                          UpdateEmailSerializer, UpdatePasswordSerializer,
                          UserSerializer)

no_response = openapi.Response("No response")
logout_response = openapi.Response("No response")
logout_request = openapi.Schema(type="no_body")


class UsersViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    SendEmailMixin,
    GenericViewSet,
):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    email_classes = {
        "signup": ActivationEmail,
        "activation": ConfirmationEmail,
        "resend_activation": ActivationEmail,
        "update_email": ActivationEmail,
    }

    def get_object(self):
        if self.action in ["me", "patch_me", "update_password", "update_email"]:
            return self.request.user

        return super().get_object()

    def get_serializer_class(self):
        if self.action == "partial_update":
            return MeSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "partial_update":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    @action(methods=["post"], detail=False)
    def signup(self, request):
        return self.create(request)

    @swagger_auto_schema(responses={"204": no_response})
    @action(methods=["post"], detail=False, serializer_class=ActivationSerializer)
    def activation(self, request):
        self.create(request)
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=["post"], detail=False, serializer_class=ResendActivationEmailSerializer
    )
    def resend_activation(self, request, *args, **kwargs):
        self.create(request)
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=False,
        serializer_class=MeSerializer,
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        return self.retrieve(request)

    @me.mapping.patch
    def patch_me(self, request):
        return self.partial_update(request)

    @action(
        methods=["patch"],
        detail=False,
        serializer_class=UpdateEmailSerializer,
        permission_classes=[IsAuthenticated],
    )
    def update_email(self, request):
        return self.update(request)

    @action(
        methods=["patch"],
        detail=False,
        serializer_class=UpdatePasswordSerializer,
        permission_classes=[IsAuthenticated],
    )
    def update_password(self, request):
        return self.update(request)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TokenViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = TokenSerializer

    @action(methods=["post"], detail=False)
    def login(self, request):
        return self.create(request)

    @swagger_auto_schema(
        responses={"204": logout_response}, request_body=logout_request
    )
    @action(methods=["post"], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        request.user.logout()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class SocialAuthViewSet(SendEmailMixin, GenericViewSet):
#     email_classes = {"google": GoogleAuthNewUserCreated}
#
#     @action(methods=["post"], detail=False, serializer_class=GoogleAuthSerializer)
#     def google(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user_email = serializer.id_info["email"]
#
#         user = User.objects.get_object_or_none(email=user_email)
#         if user is None:
#             password = token_urlsafe(16)
#             user = User.objects.create_user(email=user_email, password=password)
#             user.is_active = True
#             user.save()
#             self.send_email(user, {"email": user_email, "password": password})
#         token = user.login()
#         return Response(TokenSerializer(token).data, status=status.HTTP_200_OK)
