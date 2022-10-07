from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255)
    cat_img=models.ImageField(upload_to='images/category', blank=True)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name='Categorys'
        verbose_name_plural='Categories'
    def get_url(self):
        return reverse('category_product',args=[self.slug])
