from django.shortcuts import render,redirect,get_object_or_404
from Store.models import Product
from .models import Cart,CartItem
from django.http import HttpResponse

# Create your views here.
def _card_id(request):
    cart=request.session.session_key
    if not cart:
        #pass
        cart=request.session.create()
    return cart
def add_cart(request,product_id):
    if request.method=='POST':
        color=request.POST['color']
        size=request.POST['size']
        print(color,size)
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_card_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_card_id(request)
        )
    cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity=cart_item.quantity+1
        #cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
    cart_item.save()
    #return HttpResponse(cart_item.product)
    return redirect('/cart')
def remove_cart(request,product_id):
    cart=Cart.objects.get(cart_id=_card_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity>1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('/cart')
def remove_cart_item(request,product_id):
    cart=Cart.objects.get(cart_id=_card_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('/cart')
def cart(request,total=0,quantity=0,cart_item=None):
    cart=Cart.objects.get(cart_id=_card_id(request))
    cart_item=CartItem.objects.filter(cart=cart,is_available=True)
    for ci in cart_item:
        total=total+ci.product.price*ci.quantity
        #quantity=quantity+ci.quantity
    tax=(5*total)/100
    grand_total=tax+total
    return render(request,'cart.html',{'cart_item':cart_item,'total':total,'tax':tax,'gtotal':grand_total})
