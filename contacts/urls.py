from django.urls import path
from django.http import HttpResponse, request
from . import views

urlpatterns = [
    path('', views.contact, name='contacts'),
]