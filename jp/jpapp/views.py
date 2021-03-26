from django.shortcuts import render

def index(request):
  return render(request, "jpapp/index.html")

def home(request):
    return render(request, "jpapp/home.html")