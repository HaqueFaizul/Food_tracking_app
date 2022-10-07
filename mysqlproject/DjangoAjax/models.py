from django.db import models

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=30)
class State(models.Model):
    country=models.IntegerField()
    state_name=models.CharField(max_length=30)
