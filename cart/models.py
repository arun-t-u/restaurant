from django.db import models
from django.db.models.fields.related import ForeignKey
from shop.models import *

# Create your models here.


class cart_list(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class item(models.Model):
    product=ForeignKey(products,on_delete=models.CASCADE)
    cart=ForeignKey(cart_list,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product

    def total(self):
        return self.product.price*self.quantity