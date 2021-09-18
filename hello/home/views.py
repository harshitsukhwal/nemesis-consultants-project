from django.shortcuts import render, HttpResponse

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


# Create your views here.
