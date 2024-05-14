from django.shortcuts import render
from django.http import HttpResponse

def hello(render):
     return HttpResponse('<h1>Hello Paruyr!</h1>')
 
def about(request):
    return HttpResponse('<h1>À propos de nous</h1> <p>Nous adorons merch !</p>')
def contact(request):
    return HttpResponse('<h1>Bonjour!</h1> <p>Contact us!</p>')
def help(request):
    return HttpResponse('<h1>Help</h1> <p>Help</p>')
# Create your views here.
