from django.urls import path
from . import views

urlpatterns = [
    path('/s', views.player),
]
