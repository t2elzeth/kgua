from django.urls import path

from . import views

urlpatterns = [
    path("", views.NewsListAPIView.as_view()),
    path("<int:pk>/", views.NewsDetailAPIView.as_view()),
]
