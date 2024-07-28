from django.contrib import admin
from django.urls import path

from . import views

app_name = "landpage"

urlpatterns = [
    path('', views.home, name='home'),
    path('thanks/', views.thanks, name='thanks'),
]
