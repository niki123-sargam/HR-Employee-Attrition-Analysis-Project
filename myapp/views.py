from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def getdata(request):
    return render(request,"getdata.html")

def descriptive(request):
    return render(request,"descriptive.html")


def predictive(request):
    return render(request,"predictive.html")

