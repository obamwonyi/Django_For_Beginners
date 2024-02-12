from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    """
    Function base view,
    Handles the home view 
    """
    return HttpResponse("Hello, World")
