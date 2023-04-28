from django.shortcuts import render
from django.http import HttpResponse

def landing_page_index(request):
    return HttpResponse("Hey! It works!")