from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from medical_data_managemnt.settings import BASE_DIR

# Create your views here.

def display_home_page(request):

    return render(request, 'index.html')

def signup(request):

    pass

def login(request):

    username = request.POST['username']
    passwd = request.POST['passwd']

    user = auth.authenticate(username=username, password=passwd)

    if user is not None:

        auth.login(request, user)
        print("logged in")
        return render(request, 'login.html')
    
    else:
        messages.info(request, 'Invalid credentials')
        print("Invalid")
        return redirect("/")


