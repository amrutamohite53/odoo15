from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(response):
    return HttpResponse("This message is from Products App") 