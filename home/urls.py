from django.urls import path
from donate import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]