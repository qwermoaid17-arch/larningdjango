from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('master/', views.master, name='master'),
    path('apises/', views.apises, name='apises'),
    path('template/', views.template, name='template'),
    path('about/', views.about, name='about'),
]