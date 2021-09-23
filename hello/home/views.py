from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from home.models import credentials

def index(request):
    context ={
        "variable": "Welcome to Django",
        "variable": "Made by Harshit Sukhwal"
    }
    return render (request,'index.html',context)

    #return HttpResponse ("This is the homepage")

def about(request):
        return render (request,'about.html')
    #return HttpResponse("This is the about page")

def services(request):
    return render (request,'services.html')
    #return HttpResponse("This is the service page")

def contact(request):
    return render (request,'contact.html')
    
    #return HttpResponse("This is the contact page")
def credentials(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone =request.POST.get('phone')
        email =request.POST.get('email')
        address =request.POST.get('address')
        credentials = credentials(name=name,email=email, phone =phone,address=address, date=datetime.today() )
        credentials.save()
        
    return render (request,'credentials.html')



# Create your views here.
