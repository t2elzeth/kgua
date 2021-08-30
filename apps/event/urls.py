from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListAPIView.as_view(), name='event-list'),
    path("<int:pk>/", views.EventDetailAPIView.as_view(), name='event-detail')
]
