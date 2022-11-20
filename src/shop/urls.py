from django.urls import path

from shop.views import (BasketView,  OrderCreateView,
                        basket_add, basket_remove,
                        generate_category_view, generate_product_view,
                        generate_sub_category_view)

app_name = "shop"

urlpatterns = [
    path("category", generate_category_view, name="generate_category"),
    path("sub-category", generate_sub_category_view, name="generate_sub_category"),
    path("products", generate_product_view, name="generate_products"),
    path("add/<int:pk>", basket_add, name="add_to_basket"),
    path("remove/<int:pk>", basket_remove, name="remove_from_basket"),
    path("show", BasketView.as_view(), name="show_basket"),
    path("create", OrderCreateView.as_view(), name="order_create"),
]
