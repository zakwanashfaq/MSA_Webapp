from . import views
from django.http import request


def donate_click():
    views.donate_home(request)