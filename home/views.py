from django.shortcuts import render

from django.http import HttpResponse, request


def index(request):
    return render(request,'home.html')


# Create your views here.
