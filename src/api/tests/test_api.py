from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient

from core.utils.samples import sample_category, sample_user


class TestApi(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        # simple user
        self.user = sample_user(**{"email": "test@test.com", "phone": "+380668145993"})
        self.user.set_password("password")
        self.user.save()

        # content manager user
        self.user_content_manager = sample_user(
            **{"email": "content@content.com", "phone": "+380668145992", "is_content": True}
        )
        self.user_content_manager.set_password("password")
        self.user_content_manager.save()

        # admin user
        self.admin = sample_user(**{"email": "admin@admin.com", "phone": "+380668145991", "is_staff": True})
        self.admin.set_password("password_admin")
        self.admin.save()

        # sample category
        self.name_category = "test API category"
        self.alias_category = "tests-alias-category"
        self.category = sample_category(name=self.name_category, **{"alias": self.alias_category})

    def test_get_categories_anonymous(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:category-list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)

    def test_get_categories_admin(self):
        self.client.force_authenticate(user=self.admin)
        result = self.client.get(reverse("api:category-list"))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(result.data[0]["name"], "test API category")

    def test_get_categories_content_manager(self):
        self.client.force_authenticate(user=self.user_content_manager)
        result = self.client.get(reverse("api:category-list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)

    def test_get_category_by_alias_anonymous(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:api_category_detail", kwargs={"alias": self.alias_category}))
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(result.data["name"], self.name_category)

    def test_create_sub_category_content_manager(self):
        self.client.force_authenticate(user=self.user_content_manager)
        alias = "tests-subcategory"
        name = "API sub category"
        data = {
            "index": True,
            "name": name,
            "seo_title": "seo_title",
            "category": self.category.pk,
            "alias": alias,
        }
        create = self.client.post(reverse("api:api_create_sub_category"), data=data)
        self.assertEqual(create.status_code, HTTP_201_CREATED)
        check_get = self.client.get(reverse("api:api_sub_category_detail", kwargs={"alias": alias}))
        self.assertEqual(check_get.data["name"], name)
