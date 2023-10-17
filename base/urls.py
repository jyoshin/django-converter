from django.urls import path
from . import views

urlpatterns = [
    path('', views.basicResponse, name='tasks'),
]