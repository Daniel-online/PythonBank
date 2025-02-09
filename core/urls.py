from django.contrib import admin
from django.urls import path
from core import views as core_view

app_name='core'

urlpatterns = [

    path('contatos/', core_view.contatos),
    path('logout/', core_view.logout),
    path('extrato/', core_view.extrato),
    path('sobre_nos/', core_view.sobre_nos),
    path('sua_conta/', core_view.sua_conta),
  
]

