from django.shortcuts import render

# Create your views here.

def fill_form(request):

    return render(request, "fill_form.html")
