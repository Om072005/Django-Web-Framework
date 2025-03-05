from django.urls import path
from . import views

from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1> ")

