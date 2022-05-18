from django.http import HttpResponse
from django.shortcuts import render
#from django.template.loader import get_template

def login(request):
    
    #cargador = get_template('login.html')
    #plantillaLogin=cargador.render()    
    return render(request, 'login.html')