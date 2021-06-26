from django.urls import path

from . import views

urlpatterns = [
    path("events/", views.EventListAPIView.as_view()),
    path("promotions/", views.PromotionListAPIView.as_view()),
    path("charities/", views.CharityListAPIView.as_view()),
]
