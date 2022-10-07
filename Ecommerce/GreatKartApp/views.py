from django.shortcuts import render,redirect
from Store.models import Product
# Create your views here.
def HomePage(request):
        product = Product.objects.all().filter(is_available=True)
        return render(request, 'HomePage.html', {'product': product})

