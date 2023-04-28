from django.shortcuts import render, HttpResponse

# Create your views here.

def display_home_page(request):

    return HttpResponse("<b>welcome</b>")
