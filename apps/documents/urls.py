from django.urls import path

from . import views

urlpatterns = [
    path("for_application/", views.ApplicationDocumentListAPIView.as_view()),
]
