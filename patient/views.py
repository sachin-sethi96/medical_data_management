from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient

# Create your views here.

def fill_form(request):

    return render(request, "fill_form.html")

def register(request):

    if request.method == "POST":

        email = request.POST['email']
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        contact_number = request.POST['area_code'] + request.POST['number']
        is_whatsapp_num = True if request.POST['is_whatsapp_num'] == "on" else False
        location = request.POST['location']
        registered_by = request.user.username

        patient_object = Patient(email=email, name=name, age=age, gender=gender, contact_number=contact_number, 
                                 is_whatsapp_num=is_whatsapp_num, location=location, registered_by=registered_by)
        patient_object.save()

        messages.info(request, "User registered!!")

        return redirect("/registration/fill_form")
