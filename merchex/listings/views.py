from django.shortcuts import render
from django.http import HttpResponse

def hello(render):
     return HttpResponse('<h1>Hello Paruyr!</h1>')
 
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
# Create your views here.
