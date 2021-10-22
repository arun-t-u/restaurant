from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.searching, name='search'),
    path('<slug:cat_slug>/',views.index,name='product_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.product_details,name='pdt_detail'),
    
]
