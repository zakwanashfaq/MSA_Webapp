from django.shortcuts import render
from django.http import HttpResponse, request


def about(request):
    return render(request, 'about.html')

# Create your views here.