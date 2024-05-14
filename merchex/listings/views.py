from django.shortcuts import render
from django.http import HttpResponse

def hello(render):
     return HttpResponse('<h1>Hello Paruyr!</h1>')

# Create your views here.
