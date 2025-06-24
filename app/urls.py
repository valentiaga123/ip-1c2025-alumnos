from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('filter_by_type/', views.filter_by_type, name='filter_by_type'),

    path('login/', views.iniciar_sesion, name='login'),
    path('register/', views.registrar_usuario, name='register'),

    path('spinner/', views.spinner, name='spinner'),

    path('exit/', views.cerrar_sesion, name='exit'),
]
