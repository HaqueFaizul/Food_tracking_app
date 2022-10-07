from django.db import models
from django.db.models import CharField


class Book(models.Model):
    Book_Name: CharField=models.CharField(max_length=20)
    Book_author=models.CharField(max_length=20)
    Cover_page=models.ImageField(upload_to='CoverPage')
    E_book = models.FileField(upload_to='Ebook')
