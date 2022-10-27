"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from shop.views import CategoryView, SubCategoryView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("core.urls")),
    re_path(r'^(?P<category_name>[-\w]+)$', CategoryView.as_view(), name="category_view"),
    re_path(r'^(?P<category_name>[-\w]+)/(?P<sub_category_name>[-\w]+)$', SubCategoryView.as_view(), name="category_view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
