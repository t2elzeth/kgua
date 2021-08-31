from django.urls import path

from . import views

urlpatterns = [
    path("", views.JubileeListAPIView.as_view()),
    path("<int:pk>/", views.JubileeDetailAPIView.as_view()),
]
