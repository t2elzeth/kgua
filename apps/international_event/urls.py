from django.urls import path

from . import views

urlpatterns = [
    path("", views.InternationalEventListAPIView.as_view(), name='InternationalEvent-list'),
    path("<int:pk>/", views.InternationalEventDetailAPIView.as_view(), name='InternationalEvent-detail')
]
