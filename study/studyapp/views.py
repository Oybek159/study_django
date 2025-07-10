from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Study Django App!")

def room(request):
    return HttpResponse("This is the room page.")
