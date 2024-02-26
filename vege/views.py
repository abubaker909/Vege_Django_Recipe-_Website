from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def post(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        #print(receipe_image)
        #print(receipe_name)
        #print(receipe_description)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )

        return redirect('/getAll/')

    return render(request , "receipes.html")

def getAll(request):
    queryset = Receipe.objects.all()
    context = {'receipes' : queryset}
    return render(request, "allReceipes.html" , context)

def delete(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete() 
    return redirect('/getAll/')

def update(request, id):
    queryset = Receipe.objects.get(id = id)

    
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()

        return redirect('/getAll/')

    context = {'receipe' : queryset}


    return render(request, "updateReceipe.html", context)

def getOne(request, id):
    queryset = Receipe.objects.get(id = id)
    context = {'receipe' : queryset}
    return render(request,  "oneReceipe.html", context)
