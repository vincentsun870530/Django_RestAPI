from django.urls import path
from rest_framework import routers
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
