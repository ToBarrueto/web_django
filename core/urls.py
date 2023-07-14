from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns=[
    path('', views.base, name="base"),
    path('index', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.contacto, name="contacto"),
    path('api', views.api, name="api"),

    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar', views.actualizar, name="actualizar"),
    path('eliminar', views.eliminar, name="eliminar"),

    path('registro', views.registro, name="registro"),
    path('logout', views.cerrarsesion, name="logout"),
    path('iniciar', views.iniciar, name="iniciar"),
    
    

     
     
     ]

