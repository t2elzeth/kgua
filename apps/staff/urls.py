from django.urls import path

from . import views

urlpatterns = [
    path("", views.StaffListAPIView.as_view()),
]
