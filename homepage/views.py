from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from medical_data_managemnt.settings import BASE_DIR

# Create your views here.

def display_home_page(request):

    return render(request, 'index.html')

def signup(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    passwd = request.POST['passwd']
    rep_passwd = request.POST['rep_passwd']

    username = email.split('@')[0]

    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=passwd)
    user.save()

    messages.info(request, "User created!!")
    return redirect('/')

def login(request):

    if request.method == "POST":

        username = request.POST['username']
        passwd = request.POST['passwd']

        user = auth.authenticate(username=username, password=passwd)

        if user is not None:

            auth.login(request, user)
            return redirect("/user_login")
        
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'user_login.html')
        
    else:
        return render(request, 'login.html')
    
def user_login(request):

    return render(request, "user_login.html")

def logout(request):

    auth.logout(request)
    return redirect("/")

