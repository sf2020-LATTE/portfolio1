from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, CompanyForm, TodoForm
from . models import Company, Todo
from .mixins import OnlyYouMixin

def index(request):
  return render(request, "jpapp/index.html")

@login_required
def home(request):
    return render(request, "jpapp/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("jpapp:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'jpapp/signup.html', context)

class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "jpapp/users/detail.html"

class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = "jpapp/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('jpapp:users_detail', pk=self.kwargs['pk'])

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "jpapp/companies/create.html"
    form_class = CompanyForm
    success_url = reverse_lazy("jpapp:companies_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = "jpapp/companies/list.html"

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "jpapp/companies/detail.html"

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = "jpapp/companies/update.html"
    form_class = CompanyForm

    def get_success_url(self):
        return resolve_url('jpapp:companies_detail', pk=self.kwargs['pk'])

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = "jpapp/companies/delete.html"
    form_class = CompanyForm
    success_url = reverse_lazy("jpapp:companies_list")


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "jpapp/Todo/create.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
