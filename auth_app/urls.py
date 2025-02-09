from django.urls import path
from django.contrib import admin
from auth_app import views as auth_views

app_name= 'auth_app'

urlpatterns=[
    path('cadastro/', auth_views.cadastro_de_usuario, name="cadastro")
]