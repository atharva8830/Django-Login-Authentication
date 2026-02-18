from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

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


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username = username, password = password)
        return redirect('home')
    return render (request,  'register.html')           