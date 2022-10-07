from django.db import models
from Category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    slug        =models.SlugField(max_length=100,unique=True)
    description =models.TextField(max_length=255)
    images      =models.ImageField(upload_to='images/product')
    price       =models.IntegerField()
    stock       =models.IntegerField()
    category    =models.ForeignKey(Category,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug])
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_available=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_available=True)
Variation_pro_drop=(
    ('color','color'),
    ('size','size'),
)
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=Variation_pro_drop)
    variation_value=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)

    objects=VariationManager()

    def __unicode__(self):
        return self.product

