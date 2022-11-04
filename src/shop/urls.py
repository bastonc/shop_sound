from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from shop.views import CategoryView, SubCategoryView, generate_category_view, generate_sub_category_view, generate_product_view

app_name = "shop"

urlpatterns = [
    path("category/", generate_category_view, name="generate_category"),
    path("sub-category/", generate_sub_category_view, name="generate_sub_category"),
    path("products/", generate_product_view, name="generate_products"),
]
