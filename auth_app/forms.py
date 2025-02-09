from django import forms
from django.contrib.auth.forms import UserCreationForm
from auth_app.models import User


class CadastroDeUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email',' password1', 'password2']
        