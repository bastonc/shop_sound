from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import (CategoriesDetailView, CategoriesView, ProductDetailView,
                       ProductViewSet, SubCategoriesDetailView,
                       SubCategoriesViewSet, UserViewSet, ProductDeleteView)

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
    path("products/delete/<int:pk>", ProductDeleteView.as_view(), name="delete_record"),
    path("sub-category/<str:alias>/", SubCategoriesDetailView.as_view(), name="api_sub_category_detail"),
    path("category/<str:alias>/", CategoriesDetailView.as_view(), name="api_category_detail"),
]
