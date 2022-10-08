from django.shortcuts import render
from django_rest import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customers
from api.serializers import (CategorySerializer, CustomerSerializer, ProductSerializer,
                             SubCategorySerializer, SubCategoryCreateSerializer)
from shop.models import Category, Product, SubCategory


# User views
class UserViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class UserCreateSet(CreateAPIView):
    queryset = Customers


# Product views
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get("pk"))


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# SubCategory views
class SubCategoriesViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoriesDetailView(RetrieveAPIView):
    serializer_class = SubCategorySerializer

    def get_object(self):
        return SubCategory.objects.get(alias=self.kwargs.get("alias"))


class SubCategoryDeleteView(DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryUpdateView(UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryCreateView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateSerializer



# Category views
class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesDetailView(RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_object(self):
        return Category.objects.get(alias=self.kwargs.get("alias"))


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

