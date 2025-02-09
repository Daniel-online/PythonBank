from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #Dados pessoais
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    #Dados relativos a conta    
    has_debt = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
