from django.db import models

class Employee(models.Model):
    ename=models.CharField(max_length=20)
    edesg=models.CharField(max_length=20)
    esal=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

# Create your models here.
