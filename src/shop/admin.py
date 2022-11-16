from django.contrib import admin

from shop.models import Brand, Category, Order, Pages, Product, SubCategory, OrderItem


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']
#
#
# #@admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email',
#                     'address', 'postal_code', 'city', 'paid',
#                     'created', 'updated']
#     list_filter = ['paid', 'created', 'updated']
#     #inlines = [OrderItemInline]
#     # class Meta:
#     #     ordering = ('-created',)
#     #     verbose_name = 'OrderAdmin'
#     #     verbose_name_plural = 'OrdersAdmin'

# Register your tests here.
admin.site.register([Order, Category, SubCategory, Brand, Product, Pages])
