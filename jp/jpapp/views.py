from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, CompanyForm, TaskForm, BoardForm
from . models import Company, Task, Board
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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "jpapp/Tasks/create.html"
    form_class = TaskForm
    success_url = reverse_lazy("jpapp:tasks_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "jpapp/tasks/list.html"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "jpapp/tasks/detail.html"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "jpapp/tasks/update.html"
    form_class = TaskForm

    def get_success_url(self):
        return resolve_url('jpapp:tasks_detail', pk=self.kwargs['pk'])

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "jpapp/tasks/delete.html"
    form_class = TaskForm
    success_url = reverse_lazy("jpapp:tasks_list")

def boards_list(request):
    object_list = Board.objects.all()
    return render(request, 'jpapp/boards/list.html', {'object_list':object_list})

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = "jpapp/boards/create.html"
    form_class = BoardForm
    success_url = reverse_lazy("jpapp:boards_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def boards_detail(request, pk):
    object = get_object_or_404(Board, pk=pk)
    return render(request, 'jpapp/boards/detail.html', {'object':object})

class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    template_name = "jpapp/boards/update.html"
    form_class = BoardForm

    def get_success_url(self):
        return resolve_url('jpapp:boards_detail', pk=self.kwargs['pk'])
