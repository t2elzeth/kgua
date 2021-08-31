from django.urls import path

from . import views

urlpatterns = [
    path("", views.CharityListAPIView.as_view()),
    path("<int:pk>/", views.CharityDetailAPIView.as_view())
]
