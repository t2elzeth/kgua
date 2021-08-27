from django.urls import path

from . import views

urlpatterns = [
    path("", views.DepartmentListAPIView.as_view()),
]
