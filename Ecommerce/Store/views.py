from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from Category.models import Category
from Cart.models import CartItem
from Cart.views import _card_id
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Variation


# Create your views here.
def Store(request,category_slug=None):
    #categories=None
    #products=None
    if(category_slug != None):
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=categories,is_available=True)
        paginator=Paginator(products,1)
        page=request.GET.get('page')
        paged_product=paginator.get_page(page)
        product_count = products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        paginator=Paginator(products,2)
        page=request.GET.get('page')
        paged_product=paginator.get_page(page)
        product_count=products.count()
    return render(request,'Store.html',{'products':paged_product,'pcount':product_count})
def product_details(request,category_slug,product_slug):
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    add_cart=CartItem.objects.filter(cart__cart_id=_card_id(request),product=single_product).exists()
    return render(request,'Product_details.html',{'single_product':single_product,'add_cart':add_cart})
def Search(request):
    if 'keyword' in request.GET:
        keyword=request.GET.get('keyword')
        if keyword:
            products=Product.objects.order_by('created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        else:
            return redirect('store')
    return render(request,'Store.html',{'products':products,'pcount':product_count})