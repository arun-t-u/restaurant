from django.contrib import admin
from . models import *

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)

class pdtadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','category','image','price','stock','available']
    list_editable=['category','image','price','stock','available']
admin.site.register(products,pdtadmin)