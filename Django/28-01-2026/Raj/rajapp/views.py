from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def RajView(Request):
    return HttpResponse("Welcome to Raj's Django Application!")