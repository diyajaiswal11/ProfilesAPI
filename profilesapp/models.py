from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class UserProfile(AbstractBaseUser):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Favourite(models.Model):
    userid=models.CharField(max_length=10)
    category=models.CharField(max_length=255)

    def __str__(self):
        return self.category
    

