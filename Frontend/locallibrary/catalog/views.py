from django.shortcuts import render
from catalog.models import Client, Booking, Worker
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required

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

    workers = Worker.objects.filter().values()

    workersList = []
    for worker in workers:
        workersList.append((
            worker['name'] + " " + worker['surname'],
            worker['image'],
            worker['description'],
            worker['titles'].split(','), 
            worker['collaborations'].split(','),
        ))

    context = {
        'Acercade' : True,
        'showLoginLogout': True,
        'workersList':workersList
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
        dateToday = datetime.datetime.fromisoformat(datetime.datetime.today().strftime('%Y-%m-%d'))
        print(str(date) + " " + str(dateToday))
        if(date >= dateToday):
            bookings = Booking.objects.filter(startDate__range=[date,dateNextDay]).values()
            
            if(date.weekday() <= 4): #es entre semana
                startTime = 15
                endTime = 21    
            else: #finde
                startTime = 10
                endTime = 13
            
            hours = [] 
            for i in range(startTime,endTime):
                hours.append((i,i+1,False))
            
            for booking in bookings:
                position = hours.index((booking["startDate"].hour, (booking["startDate"].hour+1), False))
                if position is not None:
                    hours[position] =(booking["startDate"].hour,(booking["startDate"].hour+1), True)

            context["hours"] = hours
            context["today"] = request.POST["datepicker"]
    return render(request,'bookings.html', context=context)

@login_required
def makeBooking(request):
    context = {
        'Reservas' : True,
        'showLoginLogout': True,
    }
    if (request.method == "POST") and (request.POST["datepicker"] is not None):
        date = datetime.datetime.fromisoformat(request.POST["datepicker"])
        date += datetime.timedelta(hours=int(request.POST["bookingTime"]))
        cliente = Client.objects.get(username=request.user)

        print(str(date) + " " + str(cliente))
        Booking.objects.create(client=cliente,
                                startDate=date)

    return render(request,'bookings.html', context=context)

    