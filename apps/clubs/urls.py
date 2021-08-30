from django.urls import path

from . import views

urlpatterns = [
    path("", views.ClubListAPIView.as_view()),
    path("<int:pk>/", views.ClubDetailAPIView.as_view()),
]
