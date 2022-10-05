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


    class Meta:
        model = SubCategory
        fields = ("id", "index", "name", "alias", "seo_title", "seo_description", "seo_text", "image", "alias",
                 )


class CategorySerializer(ModelSerializer):
    cat = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #sub_categories = serializers.RelatedField(source="category", read_only=True)

    class Meta:
        model = Category
        fields = ("name", "cat")






