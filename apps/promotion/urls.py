from django.urls import path

from . import views

urlpatterns = [
    path("", views.PromotionListAPIView.as_view()),
    path("<int:pk>/", views.PromotionDetailAPIView.as_view()),
]
