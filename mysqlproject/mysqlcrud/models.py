from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50, default='')
    roll_number=models.IntegerField()
    address=models.CharField(max_length=50, default='')
    gender=models.CharField(max_length=20,default='')
    language=models.CharField(max_length=50)
    country=models.CharField(max_length=20, default='')
    studentstatus=models.TextChoices('user','ACTIVE INACTIVE')
    status=models.CharField(max_length=20, default='ACTIVE',choices=studentstatus.choices)

