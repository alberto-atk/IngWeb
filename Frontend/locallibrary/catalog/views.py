from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    context = {"1":"nav-link active"}
    return render(request, 'index.html', context=context)
# Create your views here.
