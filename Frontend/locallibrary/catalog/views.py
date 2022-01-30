from django.shortcuts import render
from django.shortcuts import redirect
from catalog.models import Client, Booking, Worker, Publication
from django.contrib.auth.models import User
import datetime
import locale
import os

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    esEditor = False
    if request.user.groups.filter(name__in=['Editor']):
        esEditor = True

    context = {
        'Inicio' : True,
        'showLoginLogout': True,
        'publications': getPublications(),
        'EditarPublicaciones': esEditor,
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
    esEditor = False
    if request.user.groups.filter(name__in=['Editor']):
        esEditor = True
    context = {
        'Contacto' : True,
        'showLoginLogout': True,
        'EditarPublicaciones': esEditor,
    }
    return render(request,'contact.html', context=context)

def aboutme(request):
    esEditor = False
    if request.user.groups.filter(name__in=['Editor']):
        esEditor = True
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
        'workersList':workersList,
        'EditarPublicaciones': esEditor,
    }
    return render(request,'aboutme.html', context=context)
    
@login_required
def bookings(request):
    esEditor = False
    if request.user.groups.filter(name__in=['Editor']):
        esEditor = True
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
        'EditarPublicaciones': esEditor,
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
    esEditor = False
    if request.user.groups.filter(name__in=['Editor']):
        esEditor = True
    client = Client.objects.get(username=request.user)
   
    context = {
        'showLoginLogout': False,
        'name': client.name,
        'username': client.username,
        'mail':client.mail,
        'surname':client.surname,
        'EditarPublicaciones': esEditor,
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

        if(request.POST['password'] != '' and request.POST['password2'] != ''):
            if (request.POST['password'] == request.POST['password2']):
                user.password = request.POST['password']
        else:
            print("Las contraseñas estan vacías")
        client.save()
        user.save()
        
    return redirect('settings')

@login_required
def editPublications(request):
    if request.user.groups.filter(name__in=['Editor']):

        context = {
            'EditarPublicaciones':True,
            'ActivarEditarPublicaciones':True,
            'showLoginLogout': True,
            'publications':getPublications(),

        }
        return render(request,'editPublications.html',context=context)
    return redirect('/')

def getPublications():
    publicationsBD = Publication.objects.filter().values()
    publications = []
    locale.setlocale(locale.LC_ALL, '') 
    for publication in publicationsBD:
        publications.append((
            publication['hashtags'],
            publication['title'],
            publication['image'],
            publication['description'],
            publication['date'].strftime("%d %b %Y %H:%M"),
            publication['id']
        ))
    return publications


def publicationDetails(request, pk):
    if pk:
        publication = Publication.objects.filter(pk=pk).values()[0]
        esEditor = False
        locale.setlocale(locale.LC_ALL, '') 
        if request.user.groups.filter(name__in=['Editor']):
            esEditor = True
        context = {
            'Inicio' : True,
            'EditarPublicaciones':esEditor,
            'showLoginLogout': True,
            'hashtags': publication['hashtags'],
            'title': publication['title'],
            'image': publication['image'],
            'content': publication['content'],
            'date': publication['date'].strftime("%d %b %Y %H:%M"),
        }
        return render(request,'publicationDetails.html', context=context)

@login_required
def deletePublication(request, pk):
    if request.user.groups.filter(name__in=['Editor']) and pk:
        publication = Publication.objects.get(pk=pk)
        publication.delete()
        return redirect('editPublications')
    return redirect('/')

@login_required
def addPublicationView(request):
    if request.user.groups.filter(name__in=['Editor']):
        context = {
            'addPublication': True,
            'EditarPublicaciones':True,
            'ActivarEditarPublicaciones':True,
        }
        return render(request,'editAddPublication.html',context=context)

    return redirect('/')


@login_required
def addPublication(request):
    if request.user.groups.filter(name__in=['Editor']) and request.method == "POST":
        publication = Publication.objects.create(
            hashtags=request.POST['hashtags'],
            title=request.POST['title'],
            description=request.POST['description'],
            content=request.POST['content'],
            date=datetime.datetime.now()
        )

        publication.image.save(request.FILES['image'].name,request.FILES['image'])
        publication.save()


        return redirect('editPublications')
    return redirect('/')



@login_required
def editPublicationView(request, pk):
    if request.user.groups.filter(name__in=['Editor']) and pk:
        publication = Publication.objects.filter(pk=pk).values()[0]

        context = {
            'editPublication': True,
            'EditarPublicaciones':True,
            'ActivarEditarPublicaciones':True,
            'id':pk,
            'hashtags': publication['hashtags'],
            'title': publication['title'],
            'image': publication['image'],
            'description': publication['description'],
            'content': publication['content'],
            'date': publication['date']
        }
        return render(request,'editAddPublication.html',context=context)

    return redirect('/')


@login_required
def editPublication(request, pk):
    if request.user.groups.filter(name__in=['Editor']) and pk:
        publication = Publication.objects.get(pk=pk)

        if request.POST['hashtags']:
            publication.hashtags = request.POST['hashtags']
        if request.POST['title']:
            publication.title = request.POST['title']
        if request.FILES:
            os.remove(publication.image.path)
            publication.image.save(request.FILES['image'].name,request.FILES['image'])
        if request.POST['description']:
            publication.description = request.POST['description']
        if request.POST['content']:
            publication.content = request.POST['content']
        if request.POST['date']:
            publication.date = request.POST['date']

        publication.save()
        return redirect('editPublications')
    return redirect('/')

