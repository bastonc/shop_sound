from django.core.exceptions import ValidationError
from django.test import TestCase

from shop.models import Brand, Category, Product, SubCategory


class TestModels(TestCase):

    def sample_category(self):
        self.category = Category.objects.create(name="Test Category name")
        return self.category

    def sample_sub_category(self):
        self.sub_category = SubCategory.objects.create(name="Test Name", category=self.sample_category())
        return self.sub_category

    def sample_brand(self):
        self.brand = Brand.objects.create(name="Test Brand")
        return self.brand

    def sample_product(self, name, price, **params):
        defaults = {"description": "test product",
                    "sub_category": self.sample_sub_category(),
                    "brand": self.sample_brand()
                    }
        defaults.update(params)
        return Product.objects.create(name=name, price=price, **defaults)

    def sample_order(self):
        ...

    def setUp(self) -> None:
        self.product = self.sample_product("Test Product", 10000)

    def tearDown(self) -> None:
        self.product.delete()

    def test_name_limit_150(self):
        with self.assertRaises(ValidationError):
            self.sample_product(name="Ch" * 151, price=10000)
