from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CategoriesDetailView, CategoriesView,
                       CategoryCreateView, CategoryDeleteView,
                       CategoryUpdateView, ProductCreateView,
                       ProductDeleteView, ProductDetailView, ProductUpdateView,
                       ProductViewSet, SubCategoriesDetailView,
                       SubCategoriesViewSet, SubCategoryCreateView,
                       SubCategoryDeleteView, SubCategoryUpdateView,
                       UserViewSet)

app_name = "api"

routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)
routes.register("products", ProductViewSet)
routes.register("sub-categories", SubCategoriesViewSet)
routes.register("categories", CategoriesView)

schema_view = get_schema_view(
    openapi.Info(
        title="Sound shop Bastonc",
        default_version="v1",
        description="Sound equipment shop Bastonc",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bastonsv@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include(routes.urls)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-docs"),
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls.jwt")),
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
