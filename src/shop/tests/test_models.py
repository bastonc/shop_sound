from uuid import UUID, uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from shop.models import Brand, Category, Order, Product, SubCategory


class TestModels(TestCase):
    def sample_category(self, name="Test Category name"):
        default = {
            "index": True,
            "seo_title": "seo_title",
            "seo_description": "seo_description",
        }
        self.category = Category.objects.create(name=name, **default)
        return self.category

    def sample_sub_category(self, name="Test Category name"):
        default = {
            "index": True,
            "seo_title": "seo_title",
            "seo_description": "seo_description",
        }
        self.sub_category = SubCategory.objects.create(name=name, category=self.sample_category(), **default)
        return self.sub_category

    def sample_brand(self, name="Test Brand"):
        default = {
            "index": True,
            "seo_title": "seo_title",
            "seo_description": "seo_description",
        }
        self.brand = Brand.objects.create(name=name, **default)
        return self.brand

    def sample_product(self, name, price, **params):
        defaults = {
            "index": True,
            "seo_title": "seo_title",
            "seo_description": "seo_description",
            "description": "test product",
            "sub_category": self.sample_sub_category(),
            "brand": self.sample_brand(),
        }
        defaults.update(params)
        return Product.objects.create(name=name, price=price, **defaults)

    def sample_order(self, **params):
        default = {"user": self.user, "order_num": uuid4()}
        default.update(params)
        self.order = Order.objects.create(**default)
        self.order.products.add(self.product)
        self.order.products.add(self.product2)
        total_price = 0
        for product in self.order.products.all():
            total_price += product.price
        self.order.total_price = total_price
        return self.order

    def setUp(self) -> None:
        self.product = self.sample_product(name="Test Product 1", price=10000)
        self.product2 = self.sample_product(name="Test Product 2", price=10000)
        self.user = User.objects.create_user("testUser", "test@test.com", "password")

    def tearDown(self) -> None:

        self.product.delete()

    def test_name_limit_150(self):
        print("-" * 50, "Test by limit name", "-" * 50)
        with self.assertRaises(ValidationError):
            self.sample_product(name="h" * 151, price=10000)

    def test_many_sub_category_in_category(self):
        category_list = []
        name_list = []
        print("-" * 50, "Test correct relation many sub categories to one category", "-" * 50)
        for i in range(10):
            name = f"category {i}"
            category_list.append(self.sample_sub_category(name=name))
            name_list.append(name)
        for i, category in enumerate(category_list, start=0):
            print(f"Sub category name: {category.name} -> Parent category: {category.category}")
            self.assertEqual(category.name, name_list[i])

    def test_create_order(self):
        print("-" * 50, "Test create order", "-" * 50)
        order = self.sample_order()
        self.assertEqual(order.total_price, 20000)
        print(f"Order {order.order_num} product: {order.products.all()} Total price: {order.total_price:>10}")
