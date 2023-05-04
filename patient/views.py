from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient

# Create your views here.

def fill_form(request):

    return render(request, "fill_form.html")

def register(request):

    if request.method == "POST":

        if len(Patient.objects.all()) :
            next_num = 1 + int(Patient.objects.all().order_by("-registration_number")[0].registration_number[2:])

        else:
            next_num = 1


        registration_number = f'SM{next_num}'
        email = request.POST['email']
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        contact_number = request.POST['area_code'] + request.POST['number']
        is_whatsapp_num = True if request.POST.get('is_whatsapp_num') else False
        location = request.POST['location']
        registered_by = request.user.username

        patient_object = Patient(registration_number=registration_number, email=email, name=name, age=age, gender=gender, 
                                 contact_number=contact_number, is_whatsapp_num=is_whatsapp_num, location=location, 
                                 registered_by=registered_by)
        patient_object.save()

        messages.info(request, "User registered!!")

        return redirect("/registration/fill_form")
    
def search_patient(request):

    patient_object = Patient.objects.all()

    return render(request, 'search_patient.html', {'patient_obj' : patient_object})
    
def get_patient_details(request):

    patient_details = Patient
