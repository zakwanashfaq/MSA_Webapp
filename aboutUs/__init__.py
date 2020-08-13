from . import views
from django.http import request

def buttonClick():
    views.about(request)