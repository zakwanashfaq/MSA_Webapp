from django.shortcuts import render
from django.http import HttpResponse, request


def prayer(request):
    return render(request, 'prayerTimes.html')

# Create your views here.
