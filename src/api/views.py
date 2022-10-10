from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customers
from api.serializers import (CategorySerializer, CustomerSerializer,
                             ProductSerializer, SubCategoryCreateSerializer,
                             SubCategorySerializer)
from core.permissions import IsContentManager
from shop.models import Category, Product, SubCategory


# User views
class UserViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class UserCreateSet(CreateAPIView):
    queryset = Customers


# Product views
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get("pk"))


class ProductDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# SubCategory views
class SubCategoriesViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoriesDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubCategorySerializer

    def get_object(self):
        return SubCategory.objects.get(alias=self.kwargs.get("alias"))


class SubCategoryDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryCreateView(CreateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateSerializer


# Category views
class CategoriesView(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer

    def get_object(self):
        return Category.objects.get(alias=self.kwargs.get("alias"))


class CategoryDeleteView(DestroyAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    permission_classes = [IsAdminUser | IsContentManager]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
