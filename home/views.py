from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    context = {'page' : 'Home'}
    return render(request , "home/index.html" , context)

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html" , context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html" , context)

def success_page(request):  
    return HttpResponse("<h1>Hey! This is a Success Page</h1>")