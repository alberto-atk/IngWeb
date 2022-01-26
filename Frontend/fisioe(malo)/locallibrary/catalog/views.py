from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    current_user = request.user
    if current_user is not None:
        context = {'Inicio':True,
                    'Acercade':False,
                    'Contacto':False,
                    'Reservas':False,
                    'user':current_user}
    else:
        context = {'Inicio':True,
                    'Acercade':False,
                    'Contacto':False,
                    'Reservas':False}
    return render(request, 'index.html', context=context)
# Create your views here.
