from django.shortcuts import render

# Create your views here.

def cadastro_de_usuario(request):
    return render(request, "auth_app/cadastro.html")