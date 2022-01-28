from django.shortcuts import render
from catalog.models import Client, Booking
from django.contrib.auth.models import User
import datetime

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

def bookings(request):
    context = {
        'Reservas' : True,
        'showLoginLogout': True,
    }

    return render(request,'bookings.html', context=context)


def getAvailableBookings(request):
    context = {
        'Reservas' : True,
        'showLoginLogout': True,
    }
    
    if (request.method == "POST") and (request.POST["datepicker"] is not None):
        date = datetime.datetime.fromisoformat(request.POST["datepicker"])
        dateNextDay = date + datetime.timedelta(days=1)
        bookings = Booking.objects.filter(startDate__range=[date,dateNextDay]).values()
        
        if(date.weekday() <= 4): #es entre semana
            startTime = 15
            endTime = 21    
        else: #finde
            startTime = 10
            endTime = 13
        
        hours = [] 
        for i in range(startTime,endTime):
            hours.append((i,False))
        
        for booking in bookings:
            position = hours.index((booking["startDate"].hour, False))
            if position is not None:
                hours[position] =(booking["startDate"].hour, True)

        context["hours"] = hours
        
    return render(request,'bookings.html', context=context)
    