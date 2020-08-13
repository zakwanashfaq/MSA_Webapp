from django.shortcuts import render
from django.http import HttpResponse, request


def executives(request):
    return render(request, 'executives.html')

# Create your views here.