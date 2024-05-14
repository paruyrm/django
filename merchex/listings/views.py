from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band

def hello(request):
     bands = Band.objects.all ()
     return HttpResponse(f"""
         <h1>Hello Django !</h1>
         <p>Mes groupes préférés sont :<p>
         <ul>
              <li>{bands[0].name}</li>
              <li>{bands[1].name}</li>
         </ul>""")
 
def about(request):
    return HttpResponse('<h1>À propos de nous</h1> <p>Nous adorons merch !</p>')
def contact(request):
    return HttpResponse('<h1>Bonjour!</h1> <p>Contact us!</p>')
def help(request):
    return HttpResponse('<h1>Help</h1> <p>Help</p>')
# Create your views here.
