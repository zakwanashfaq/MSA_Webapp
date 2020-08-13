from django.shortcuts import render
from django.http import HttpResponse, request


def contact(request):
    return render(request, 'contacts.html')

# Create your views here.