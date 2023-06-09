from django.contrib import admin
from . models import *
admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','description','price','category','image']

admin.site.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','email','phonenumber']

admin.site.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']

admin.site.register(Order)