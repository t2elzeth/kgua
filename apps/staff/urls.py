from django.urls import path

from . import views

urlpatterns = [
    path("staff/", views.StaffListAPIView.as_view()),
    path("staff/<int:pk>/", views.StaffDetailAPIView.as_view()),
]
