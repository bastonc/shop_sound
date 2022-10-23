from django.contrib import admin

from shop.models import Brand, Category, Order, Pages, Product, SubCategory

# Register your tests here.
admin.site.register([Order, Category, SubCategory, Brand, Product, Pages])
