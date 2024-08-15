from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser

class User(AbstractUser):
    citizenNumber = models.CharField(max_length=50, unique=True)
    







