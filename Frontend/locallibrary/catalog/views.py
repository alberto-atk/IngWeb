from django.shortcuts import render
from catalog.models import User
# Create your views here.

def index(request):
    """View function for home page of site."""
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
        'Inicio' : True,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def register(request):
    #data = {
    #    'form': RegisterForm()
    #}
    #TODO MIRAR VIDEOS DE DJANTO, SI NO, CIFRAR PASS

    if request.method == 'POST':
        existeUser = User.objects.filter(login=request.POST['login'])
        #user = User.objects.create_user(request.POST)
        print(existeUser)
    return render(request,'register.html')

def contact(request):
    context = {
        'Contacto' : True,
    }
    return render(request,'contact.html', context=context)


