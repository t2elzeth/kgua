from django.urls import path

from . import views

urlpatterns = [
    path("", views.BureauListAPIView.as_view()),
    path("<int:pk>/", views.BureauDetailAPIView.as_view()),
]
