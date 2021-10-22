from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def index(request,cat_slug=None):
    c_page=None
    pdt=None
    if cat_slug!=None:
        c_page=get_object_or_404(category,slug=cat_slug)
        pdt=products.objects.filter(category=c_page,available=True)
    else:
        pdt=products.objects.all().filter(available=True)
    cat=category.objects.all()
    #paginator
    paginator=Paginator(pdt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'pr':pdt,'ct':cat,'pg':pro})


# Product Detail Page
def product_details(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
        
    except Exception as e:
        raise e
    
    return render(request,'product_detail.html',{'pr':prod})



# Searchbar
def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})
