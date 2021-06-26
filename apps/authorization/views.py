from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TokenSerializer, UserSerializer


class SignUpAPIView(generics.CreateAPIView):
    """Регистрация пользователя"""

    serializer_class = UserSerializer


class LoginAPIView(generics.CreateAPIView):
    """Войти в аккаунт"""

    serializer_class = TokenSerializer


class LogOutAPIView(APIView):
    """Выйти из аккаунта"""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.logout()
        return Response(status=status.HTTP_204_NO_CONTENT)
