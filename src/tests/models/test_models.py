from uuid import UUID, uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import (sample_order, sample_product,
                                sample_sub_category)
from shop.models import Brand, Category, Order, Product, SubCategory


class TestModels(TestCase):
    def setUp(self) -> None:
        self.product = sample_product(name="Test Product 1", price=10000)
        self.product2 = sample_product(name="Test Product 2", price=10000)
        self.user = get_user_model().objects.create(email="test@test.com")
        self.user.set_password("password")
        self.user.save()

    def tearDown(self) -> None:

        self.product.delete()

    def test_name_limit_150(self):
        print("-" * 50, "Test by limit name", "-" * 50)
        with self.assertRaises(ValidationError):
            sample_product(name="h" * 151, price=10000)

    def test_many_sub_category_in_category(self):
        category_list = []
        name_list = []
        print("-" * 50, "Test correct relation many sub categories to one category", "-" * 50)
        for i in range(10):
            name = f"category {i}"
            category_list.append(sample_sub_category(name=name))
            name_list.append(name)
        for i, category in enumerate(category_list, start=0):
            print(f"Sub category name: {category.name} -> Parent category: {category.category}")
            self.assertEqual(category.name, name_list[i])

    def test_create_order(self):
        print("-" * 50, "Test create order", "-" * 50)
        order = sample_order(self.user, self.product, self.product2)
        self.assertEqual(order.total_price, 20000)
        print(f"Order {order.order_num} product: {order.products.all()} Total price: {order.total_price:>10}")
