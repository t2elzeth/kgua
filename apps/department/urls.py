from django.urls import path

from . import views

urlpatterns = [
    path("", views.DepartmentListAPIView.as_view()),
    path("<int:pk>/", views.DepartmentDetailAPIView.as_view()),
]
