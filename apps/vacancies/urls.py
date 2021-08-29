from django.urls import path

from . import views

urlpatterns = [
    path("", views.VacancyListAPIView.as_view()),
    path("<int:pk>/", views.VacancyDetailAPIView.as_view()),
]
