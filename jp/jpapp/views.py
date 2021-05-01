from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OnlyYouMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, CompanyForm,InterviewForm, TaskForm, BoardForm, CommentForm
from . models import Company,Interview, Task, Board, Comment, Tag, Schedule
# from .mixins import OnlyYouMixin

from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm

UserModel = get_user_model( )

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

class UserDetailView(OnlyYouMixin,DetailView):
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

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser: # スーパーユーザの場合、リストにすべてを表示する。
            company_list = Company.objects.all()
            for company in company_list:
                company.tag_list = company.tag.all().select_related()
            return company_list

        else: # 一般ユーザは自分のレコードのみ表示する。
            company_list = Company.objects.filter(user=current_user.id)
            for company in company_list:
                company.tag_list = company.tag.all().select_related()
            return company_list

# def companies_list(request):
#     company_list = Company.objects.all()
#     return render(request, 'jpapp/companies/list.html', {'company_list':company_list})

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

class InterviewCreateView(LoginRequiredMixin, CreateView):
    model = Interview
    template_name = "jpapp/interviews/create.html"
    form_class = InterviewForm
    success_url = reverse_lazy("jpapp:interviews_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(InterviewCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class InterviewListView(LoginRequiredMixin, ListView):
    model = Interview
    template_name = "jpapp/interviews/list.html"

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser: # スーパーユーザの場合、リストにすべてを表示する。
            interview_list = Interview.objects.all()
            return interview_list
        else: # 一般ユーザは自分のレコードのみ表示する。
            interview_list = Interview.objects.filter(user=current_user.id)
            return interview_list


class InterviewDetailView(LoginRequiredMixin, DetailView):
    model = Interview
    template_name = "jpapp/interviews/detail.html"

class InterviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Interview
    template_name = "jpapp/interviews/update.html"
    form_class = InterviewForm

    def get_success_url(self):
        return resolve_url('jpapp:interviews_detail', pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super(InterviewUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class InterviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Interview
    template_name = "jpapp/interviews/delete.html"
    form_class = InterviewForm
    success_url = reverse_lazy("jpapp:interviews_list")

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "jpapp/tasks/create.html"
    form_class = TaskForm
    success_url = reverse_lazy("jpapp:tasks_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "jpapp/tasks/list.html"

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser: # スーパーユーザの場合、リストにすべてを表示する。
            task_list = Task.objects.all()
            return task_list
        else: # 一般ユーザは自分のレコードのみ表示する。
            task_list = Task.objects.filter(user=current_user.id)
            return task_list

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
    #object = get_object_or_404(Board, pk=pk)
    #return render(request, 'jpapp/boards/detail.html', {'object':object})

    #コメント
    board = get_object_or_404(Board, id=pk)

    comments = Comment.objects.filter(board=board).order_by('-created_at')
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(board=board, user=request.user, text=text)
            comment.save()
            #return redirect('jpapp:detail', board_id=board.id)
    else:
        form = CommentForm()
    context = {
        'board': board,
        'comments': comments,
        'form': form,
    }
    if request.is_ajax():
       html = render_to_string('jpapp/comment.html', context, request=request )
       return JsonResponse({'form': html})    
    return render(request, 'jpapp/boards/detail.html', {'board': board, 'form': form, 'comments': comments})

#コメント削除
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('jpapp:boards_detail', pk=comment.board.id)

class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    template_name = "jpapp/boards/update.html"
    form_class = BoardForm

    def get_success_url(self):
        return resolve_url('jpapp:boards_detail', pk=self.kwargs['pk'])

class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    template_name = "jpapp/boards/delete.html"
    form_class = BoardForm
    success_url = reverse_lazy("jpapp:boards_list")

def guest_login(request):
    guest_user = UserModel.objects.get(username='ゲストユーザー')
    login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('jpapp:home')


class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'jpapp/month_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class MonthWithScheduleCalendarCreateView(mixins.MonthWithScheduleMixin, CreateView):
    model = Schedule
    template_name = "jpapp/month_with_schedule/create.html"
    form_class = BS4ScheduleForm
    success_url = reverse_lazy("jpapp:month_with_schedule")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MonthWithScheduleCalendarCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MonthWithScheduleCalendarDetailView(mixins.MonthWithScheduleMixin, DetailView):
    model = Schedule
    template_name = "jpapp/month_with_schedule/detail.html"

class MonthWithScheduleCalendarUpdateView(mixins.MonthWithScheduleMixin, UpdateView):
    model = Schedule
    template_name = "jpapp/month_with_schedule/update.html"
    form_class = BS4ScheduleForm

    def get_success_url(self):
        return resolve_url('jpapp:month_with_schedule_detail', pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super(MonthWithScheduleCalendarUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MonthWithScheduleCalendarDeleteView(mixins.MonthWithScheduleMixin, DeleteView):
    model = Schedule
    template_name = "jpapp/month_with_schedule/delete.html"
    success_url = reverse_lazy("jpapp:month_with_schedule")
