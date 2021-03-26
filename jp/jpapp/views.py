from django.contrib.auth import login # 追加
from django.contrib.auth.forms import UserCreationForm # 追加
from django.shortcuts import render,redirect

def index(request):
  return render(request, "jpapp/index.html")

def home(request):
    return render(request, "jpapp/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("jpaap:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'jpapp/signup.html', context)