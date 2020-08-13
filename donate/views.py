from django.shortcuts import render
from django.http import HttpResponse, request


def donate_home(request):
    return render(request, 'donate.html')

# Create your views here.