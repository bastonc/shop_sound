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

from accounts.views import (ActivateUser, EditProfileView, Login, Logout,
                            ProfileView, Registration)
from shop.views import (CategoryView, HistoryOrderUser, ProductView,
                        SubCategoryView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("core.urls")),
    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
    path("user", Registration.as_view(), name="user"),
    path("activate/<str:uuid64>/<str:token>", ActivateUser.as_view(), name="activate_user"),
    path("accounts/profile", ProfileView.as_view(), name="profile"),
    path("edit-profile/<int:pk>/", EditProfileView.as_view(), name="edit_profile"),
    path("order-history/<int:pk>", HistoryOrderUser.as_view(), name="orders_history_user"),
    # path("generate/", include("shop.urls")),
    path("basket/", include("shop.urls")),
    re_path(r"^(?P<category_name>[-\w]+)$", CategoryView.as_view(), name="category_view"),
    re_path(
        r"^(?P<category_name>[-\w]+)/(?P<sub_category_name>[-\w]+)$",
        SubCategoryView.as_view(),
        name="sub_category_view",
    ),
    re_path(
        r"^(?P<category_name>[-\w]+)/(?P<sub_category_name>[-\w]+)/(?P<alias_item>[-\w]+)/(?P<pk_item>[-\d]+)$",
        ProductView.as_view(),
        name="product_view",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
