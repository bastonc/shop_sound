from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import (CategoriesDetailView, CategoriesView, ProductDetailView,
                       ProductViewSet, SubCategoriesDetailView, SubCategoriesViewSet,
                       UserViewSet, ProductDeleteView, ProductCreateView, ProductUpdateView,
                       SubCategoryDeleteView, SubCategoryUpdateView, SubCategoryCreateView,
                       CategoryCreateView, CategoryDeleteView, CategoryUpdateView)


app_name = 'api'

routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)
routes.register("products", ProductViewSet)
routes.register("sub-categories", SubCategoriesViewSet)
routes.register("categories", CategoriesView)



urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="api_products_detail"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="api_delete_product"),
    path("product/create/", ProductCreateView.as_view(), name="api_create_product"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="api_update_product"),
    path("sub-category/create/", SubCategoryCreateView.as_view(), name="api_create_sub_category"),
    path("sub-category/<str:alias>/", SubCategoriesDetailView.as_view(), name="api_sub_category_detail"),
    path("sub-category/delete/<int:pk>/", SubCategoryDeleteView.as_view(), name="api_delete_sub_category"),
    path("sub-category/update/<int:pk>/", SubCategoryUpdateView.as_view(), name="api_update_sub_category"),
    path("category/create/", CategoryCreateView.as_view(), name="api_create_category"),
    path("category/<str:alias>/", CategoriesDetailView.as_view(), name="api_category_detail"),
    path("category/delete/<int:pk>/", CategoryDeleteView.as_view(), name="api_delete_category"),
    path("category/update/<int:pk>/", CategoryUpdateView.as_view(), name="api_update_category"),

]
