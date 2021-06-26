from django.urls import path

from . import views

urlpatterns = [
    path("events/", views.InternationalEventListAPIView.as_view()),
    path("programs/", views.InternationalProgramListAPIView.as_view()),
    path("partners/", views.PartnerOrganizationListAPIView.as_view()),
]
