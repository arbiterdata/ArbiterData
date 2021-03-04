from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    #return render(request, "home.html", {})

    return render(request, "home.html", {})

def automation_view(request, *args, **kwargs):
    return render(request, "automation.html", {})

def PowerBI_view(request, *args, **kwargs):
    return render(request, "powerbi.html", {})

def consulting_view(request, *args, **kwargs):
    return render(request, "consulting.html", {})

def data_view(request, *args, **kwargs):
    return render(request, "data.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})