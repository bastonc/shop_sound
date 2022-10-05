from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from accounts.models import Customers
from api.serializers import CustomerSerializer, ProductSerializer, SubCategorySerializer, CategorySerializer
from shop.models import Product, SubCategory, Category


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


# SubCategory views

class SubCategoriesViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoriesDetailView(RetrieveAPIView):
    serializer_class = SubCategorySerializer

    def get_object(self):
        return SubCategory.objects.get(alias=self.kwargs.get("alias"))


# Category views

class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesDetailView(RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_object(self):
        return Category.objects.get(alias=self.kwargs.get("alias"))
