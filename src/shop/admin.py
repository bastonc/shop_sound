from django.contrib import admin

from shop.models import (Brand, Category, Order, OrderItem, Pages, Product,
                         SubCategory)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("user", "product", "price", "quantity")
    extra = 0



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'get_total_cost')
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'url', 'id']
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
# # Register your tests here.
admin.site.register([OrderItem, Category, SubCategory, Brand, Pages])
