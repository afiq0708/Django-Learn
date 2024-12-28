from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to TestDjango" )

def Course(request):
    return HttpResponse("Welcome to TestDjango" )

def courseInfo(request,courseid):
    return HttpResponse(courseid)