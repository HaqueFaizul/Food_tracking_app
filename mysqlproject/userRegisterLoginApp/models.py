from django.db import models

class Signup(models.Model):
    first_name=models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=20, default='')

# Create your models here.
