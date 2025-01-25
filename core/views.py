from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "core/index.html")

def contatos(request):
    return render(request, "core/contatos.html")

def sobre_nos(request):
    return render(request,"core/sobre_nos.html")

def logout(request):
    return render(request,"core/logout.html")

def sua_conta(request):
    return render(request,"core/sua_conta.html")

def extrato(request):
    return render(request, "core/extrato.html")
