
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
   
    path('', views.index,name='home'),
    path('presentation/', views.presentation,name='presentation'),
    path('services/', views.services,name='services'),
    path('formations/', views.formations,name='formations'),
    path('contacts', views.contact,name='contact'),

]
