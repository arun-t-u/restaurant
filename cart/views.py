from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from shop . models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod= products.objects.get(id=product_id)
    try:
        ct=cart_list.objects.get(cart_id=c_id(request))
    except cart_list.DoesNotExist:
        ct=cart_list.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=item.objects.get(product=prod,cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
        c_items.save()
    except item.DoesNotExist:
        c_items=item.objects.create(product=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('CartDetails')


def cart_details(request,total=0,count=0,gt=0,cart_items=True):
    try:
        ct=cart_list.objects.get(cart_id=c_id(request))
        ct_items=item.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total+=(i.product.price*i.quantity)
            gt=total+30
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':total,'cn':count,'gt':gt})



def min_cart(request,product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prodt= get_object_or_404(products,id=product_id)
    c_items = item.objects.get(product=prodt,cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('CartDetails')

def cart_delete(request,product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prodt= get_object_or_404(products,id=product_id)
    c_items = item.objects.get(product=prodt,cart=ct)
    c_items.delete()
    return redirect('CartDetails')