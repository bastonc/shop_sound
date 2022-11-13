from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from shop.views import CategoryView, SubCategoryView, generate_category_view, generate_sub_category_view, \
    generate_product_view, basket_add, basket_remove, BasketView

app_name = "shop"

urlpatterns = [
    path("category", generate_category_view, name="generate_category"),
    path("sub-category", generate_sub_category_view, name="generate_sub_category"),
    path("products", generate_product_view, name="generate_products"),
    path("add/<int:pk>", basket_add, name="add_to_basket"),
    path("remove/<int:pk>", basket_remove, name="remove_from_basket"),
    path("show", BasketView.as_view(), name="show_basket"),


]
