from django.contrib import admin

from shop.models import Brand, Category, Order, Product, SubCategory

# Register your models here.
admin.site.register([Order, Category, SubCategory, Brand, Product])
