from django.urls import path

from . import views

urlpatterns = [path("events/", views.EventListAPIView.as_view())]
