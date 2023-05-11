from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient, Medication

# Create your views here.

def fill_form(request):

    return render(request, "fill_form.html")

def register(request):

    if request.user.is_authenticated:

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

    return render(request, "idnex.html")

    
def search_patient(request):

    if request.user.is_authenticated:

        patient_object = Patient.objects.all()

        return render(request, 'search_patient.html', {'patient_obj' : patient_object})
        
    return render(request, "index.html")

def medicate(request, registration_id):

    if request.user.is_authenticated:
        patient_obj = Patient.objects.filter(registration_number=registration_id)[0]
        medication_obj = Medication.objects.filter(patient_id=registration_id)

        return render(request, 'medicate.html', {'patient_obj': patient_obj, 'medication_obj': medication_obj})
    
    return render(request, "index.html")

def save_medication(request, registration_id):
    
    patient_obj = Patient.objects.filter(registration_number=registration_id)[0]
    medicines_already_have = request.POST['medicines_already_have']
    medicines_recommend = request.POST['medicine_recommend']

    medication_obj = Medication(patient=patient_obj, medicines_already_have=medicines_already_have, 
                                medicines_recommend=medicines_recommend)
    
    medication_obj.save()
    return redirect('/medication/search_patient')