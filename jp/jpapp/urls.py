from django.urls import path

from . import views

app_name = "jpapp"

urlpatterns = [
    path("", views.index, name="index"),
]