from django.urls import path

from . import views

from .views import boards_list, boards_detail

app_name = "jpapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"), 
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"), 
    #Company
    path("companies/", views.CompanyListView.as_view(), name="companies_list"), 
    path("companies/create/", views.CompanyCreateView.as_view(), name="companies_create"), 
    path("companies/<int:pk>/", views.CompanyDetailView.as_view(), name="companies_detail"),
    path("companies/<int:pk>/update/", views.CompanyUpdateView.as_view(), name="companies_update"),
    path("companies/<int:pk>/delete/", views.CompanyDeleteView.as_view(), name="companies_delete"),
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
]