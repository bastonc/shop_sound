from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import Customers
from shop.models import Category, Product, SubCategory


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ("first_name", "last_name", "email", "phone", "is_staff")


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ("__all__")


class SubCategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ("id", "index", "name", "alias", "seo_title", "seo_description", "seo_text", "image",
                  "alias", "products")


class CategorySerializer(ModelSerializer):
    category = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "alias", "seo_text", "category")






