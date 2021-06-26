from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("logout/", views.LogOutAPIView.as_view()),
]
