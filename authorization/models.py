from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=32, unique = True)
    email = models.CharField(max_length=32, unique = True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length = 50, default = 'idle', blank= False, null = False)
    
    first_name = None
    second_name = None