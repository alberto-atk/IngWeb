from django.shortcuts import render
from catalog.models import Client
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    """View function for home page of site."""
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
        'Inicio' : True,
        'showLoginLogout': True,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def register(request):
    context = {
        'showLoginLogout': False,
    }
    return render(request,'register.html')

def registerUser(request):
    #YA REGISTRA, TODO preguntar a estos para redirigir bien.
    context = {        
        'Inicio' : True,
        'showLoginLogout': True,}
    if request.method == 'POST': 
        existeCliente = Client.objects.filter(login=request.POST['login'])
        if not existeCliente:
            User.objects.create_user(username=request.POST['login'],
                                   first_name=request.POST['name'],
                                   last_name=request.POST['surname'],
                                   email=request.POST['email'],
                                   password=request.POST['password'])

            Client.objects.create(login=request.POST['login'],
                                   name=request.POST['name'],
                                   surname=request.POST['surname'],
                                   mail=request.POST['email'])
            context['mensaje'] = "Usuario registrado correctamente"
            return render(request,'index.html',context)
        else:
            context['mensaje'] = "Usuario existente"
            return render(request,'index.html',context)


def contact(request):
    context = {
        'Contacto' : True,
        'showLoginLogout': True,
    }
    return render(request,'contact.html', context=context)

def aboutme(request):
    context = {
        'Acercade' : True,
        'showLoginLogout': True,
    }
    return render(request,'aboutme.html', context=context)

