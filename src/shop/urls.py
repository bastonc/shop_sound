from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from shop.views import CategoryView, SubCategoryView

app_name = "shop"

urlpatterns = [
    # re_path(r"^([a-z]*-*)$", CategoryView.as_view(), name="category_view"),
    path("", CategoryView.as_view(), name="category_view"),
    path(r"/<str:sub_category_name>", SubCategoryView, name="sub_category_view"),
    # re_path(r"^(.*\/.*)$", SubCategoryView, name="category_view"),
]
