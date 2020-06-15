from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(f"hello world from django!")

def second_base(request):
    return HttpResponse(f"hello world from django! you got to 2nd base.")
