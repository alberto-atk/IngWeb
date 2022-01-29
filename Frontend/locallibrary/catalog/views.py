from django.shortcuts import render
from django.shortcuts import redirect
from catalog.models import Client, Booking, Worker, Publication
from django.contrib.auth.models import User
import datetime
import locale

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    publications = Publication.objects.filter().values()
    publicationsModified = []
    locale.setlocale(locale.LC_ALL, '') 

    for publication in publications:
        publicationsModified.append((
            publication['hashtags'],
            publication['title'],
            publication['image'],
            publication['description'],
            publication['date'].strftime("%d %b %Y %H:%M")
        ))

    context = {
        'Inicio' : True,
        'showLoginLogout': True,
        'publications': publicationsModified
    }

    return render(request, 'index.html', context=context)

def register(request):
    context = {
        'showLoginLogout': False,
    }
    return render(request,'register.html', context=context)

def registerUser(request):
    #TODO MOSTRAR ERRORES

    if request.method == 'POST': 
        existeCliente = Client.objects.filter(username=request.POST['login'])
        print(existeCliente.count())
        print(existeCliente)
        if existeCliente.count() == 0:
            User.objects.create_user(username=request.POST['login'],
                                   first_name=request.POST['name'],
                                   last_name=request.POST['surname'],
                                   email=request.POST['email'],
                                   password=request.POST['password'])

            Client.objects.create(username=request.POST['login'],
                                   name=request.POST['name'],
                                   surname=request.POST['surname'],
                                   mail=request.POST['email'])
            print("Usuario registrado correctamente")
            return redirect('/')
        else:
            print("Usuario existente")
            return redirect('/')



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
    
@login_required
def bookings(request):

    cliente = Client.objects.get(username=request.user)

    bookings = Booking.objects.filter(client=cliente).values()

    myBookings = []
    for booking in bookings:
        myBookings.append((booking['startDate'].strftime("%d/%m/%Y %H:%M"), 
                            booking['startDate'].strftime("%Y-%m-%d %H:%M")))


    context = {
        'Reservas' : True,
        'showLoginLogout': True,
        'myBookings': myBookings,
    }
    return render(request,'bookings.html', context=context)

@login_required
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

            for hour in hours:
                if(hour[2] is False):
                    context["hours"] = hours
                    context["today"] = request.POST["datepicker"]
                    return render(request,'bookings.html', context=context)
            print("todas reservas estan ocupadas") #TODO PONER CON METODOS
    return redirect('bookings')

@login_required
def makeBooking(request):
    if (request.method == "POST") and (request.POST["datepicker"] is not None) and (request.POST["bookingTime"] is not None):
        date = datetime.datetime.fromisoformat(request.POST["datepicker"])
        date += datetime.timedelta(hours=int(request.POST["bookingTime"]))
        cliente = Client.objects.get(username=request.user)

        print(str(date) + " " + str(cliente))
        Booking.objects.create(client=cliente,
                                startDate=date)
    return redirect('bookings')

@login_required
def deleteBooking(request):
    if (request.method == "POST") and (request.POST["bookingDelete"] is not None):
        booking = Booking.objects.get(startDate=request.POST["bookingDelete"])
        booking.delete()
    return redirect('bookings')


@login_required
def settings(request):

    client = Client.objects.get(username=request.user)

    client.mail = "apbatecaz@gmail.com"    
    context = {
        'showLoginLogout': False,
        'name': client.name,
        'username': client.username,
        'mail':client.mail,
        'surname':client.surname
    }    
    
    return render(request,'settings.html', context=context)


@login_required
def changeSettings(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        client = Client.objects.get(username=request.user)
        if request.POST['username']:
            client.username = request.POST['username']
            user.username = request.POST['username']

        if request.POST['name']:
            client.name = request.POST['name']
            user.name = request.POST['name']

        if request.POST['surname']:
            client.surname = request.POST['surname']
            user.surname = request.POST['surname']      

        if request.POST['mail']:
            client.mail = request.POST['mail']
            user.email = request.POST['mail']
            print(client.mail)
            print(user.email)
            #TODO mirar porque el correo no va

        client.save()
        user.save()
        
    return redirect('settings')