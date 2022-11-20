from uuid import uuid4

from django.contrib.auth import get_user_model

from shop.models import Brand, Category, Order, Product, SubCategory


def sample_category(name="Test Category name", **params):
    default = {
        "index": True,
        "seo_title": "seo_title",
        "seo_description": "seo_description",
        "alias": "sample-category",
    }
    default.update(params)
    category = Category.objects.create(name=name, **default)
    return category


def sample_sub_category(name="Test Category name"):
    default = {
        "index": True,
        "seo_title": "seo_title",
        "seo_description": "seo_description",
    }

    sub_category = SubCategory.objects.create(name=name, category=sample_category(), **default)
    return sub_category


def sample_brand(name="Test Brand"):
    default = {
        "index": True,
        "seo_title": "seo_title",
        "seo_description": "seo_description",
    }
    brand = Brand.objects.create(name=name, **default)
    return brand


def sample_product(name, price, **params):
    defaults = {
        "index": True,
        "seo_title": "seo_title",
        "seo_description": "seo_description",
        "description": "test product",
        "sub_category": sample_sub_category(),
        "brand": sample_brand(),
    }
    defaults.update(params)
    return Product.objects.create(name=name, price=price, **defaults)


def sample_order(user, product, product2, **params):
    default = {"user": user, "order_num": uuid4()}
    default.update(params)
    order = Order.objects.create(**default)
    order.products.add(product)
    order.products.add(product2)
    total_price = 0
    for product in order.products.all():
        total_price += product.price
    order.total_price = total_price
    return order


def sample_user(**params) -> object:
    user = get_user_model().objects.create(**params)
    user.set_password("password")
    user.save()
    return user
