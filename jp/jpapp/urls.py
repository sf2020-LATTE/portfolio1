from django.urls import path

from . import views

from .views import boards_list, boards_detail, guest_login
#companies_list

app_name = "jpapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"), 
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"), 
    #Company
    path("companies/", views.CompanyListView.as_view(), name="companies_list"),
    #path("companies/", companies_list, name="companies_list"), 
    path("companies/create/", views.CompanyCreateView.as_view(), name="companies_create"), 
    path("companies/<int:pk>/", views.CompanyDetailView.as_view(), name="companies_detail"),
    path("companies/<int:pk>/update/", views.CompanyUpdateView.as_view(), name="companies_update"),
    path("companies/<int:pk>/delete/", views.CompanyDeleteView.as_view(), name="companies_delete"),
    #Interview
    path("interviews/create/", views.InterviewCreateView.as_view(), name="interviews_create"),
    path("interviews/", views.InterviewListView.as_view(), name="interviews_list"),
    path("interviews/<int:pk>/", views.InterviewDetailView.as_view(), name="interviews_detail"),
    path("interviews/<int:pk>/update/", views.InterviewUpdateView.as_view(), name="interviews_update"),
    path("interviews/<int:pk>/delete/", views.InterviewDeleteView.as_view(), name="interviews_delete"),
    #Task
    path("tasks/create/", views.TaskCreateView.as_view(), name="tasks_create"),
    path("tasks/", views.TaskListView.as_view(), name="tasks_list"),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="tasks_detail"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="tasks_update"),
    path("tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="tasks_delete"),
    #Board
    path('boards/', boards_list, name='boards_list'),
    path("boards/create/", views.BoardCreateView.as_view(), name="boards_create"),
    path('boards/<int:pk>/', boards_detail, name='boards_detail'),
    path("boards/<int:pk>/update/", views.BoardUpdateView.as_view(), name="boards_update"),
    path("boards/<int:pk>/delete/", views.BoardDeleteView.as_view(), name="boards_delete"),
    #コメント
    path('comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    #かんたんログイン用
    path('guest_login/', guest_login, name = 'guest_login'), 
    #カレンダー用
    path('month_with_schedule/',views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/',views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/create/', views.MonthWithScheduleCalendarCreateView.as_view(), name='month_with_schedule_create'),
    path('month_with_schedule/<int:pk>/', views.MonthWithScheduleCalendarDetailView.as_view(), name='month_with_schedule_detail'),
    path('month_with_schedule/<int:pk>/update/', views.MonthWithScheduleCalendarUpdateView.as_view(), name='month_with_schedule_update'),
    path('month_with_schedule/<int:pk>/delete/', views.MonthWithScheduleCalendarDeleteView.as_view(), name='month_with_schedule_delete'),
]