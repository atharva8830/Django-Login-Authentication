from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_view (request):
    return render (request , 'home.html')

def java_views(request):
    return render (request , 'java.html')

def apti_views(request):
    return render (request , 'apti.html')

@login_required
def django_views(request):
    return render (request , 'django.html')

def logout_views(request):

    return render (request , 'logout.html')