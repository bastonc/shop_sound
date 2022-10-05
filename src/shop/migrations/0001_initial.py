# Generated by Django 4.1.1 on 2022-10-03 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.BooleanField(default=True, null=True)),
                ("seo_title", models.CharField(max_length=100, null=True)),
                ("seo_description", models.CharField(max_length=300, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="static/image/products/non-image.png",
                        null=True,
                        upload_to="static/image/products/",
                    ),
                ),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brands",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.BooleanField(default=True, null=True)),
                ("seo_title", models.CharField(max_length=100, null=True)),
                ("seo_description", models.CharField(max_length=300, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                ("seo_text", models.TextField(max_length=5000, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="static/image/category/non-image.png",
                        null=True,
                        upload_to="static/image/category/",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.BooleanField(default=True, null=True)),
                ("seo_title", models.CharField(max_length=100, null=True)),
                ("seo_description", models.CharField(max_length=300, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                ("seo_text", models.TextField(max_length=5000, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="static/image/sub-category/non-image.png",
                        null=True,
                        upload_to="static/image/sub-category/",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sub category",
                "verbose_name_plural": "Sub categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.BooleanField(default=True, null=True)),
                ("seo_title", models.CharField(max_length=100, null=True)),
                ("seo_description", models.CharField(max_length=300, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                ("description", models.TextField(max_length=1500, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="static/image/products/non-image.png",
                        null=True,
                        upload_to="static/image/products/",
                    ),
                ),
                ("price", models.SmallIntegerField(null=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("UAH", "UAH"), ("USD", "USD")],
                        default="UAH",
                        max_length=3,
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="brand",
                        to="shop.brand",
                    ),
                ),
                (
                    "sub_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_category",
                        to="shop.subcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_price", models.SmallIntegerField(null=True)),
                (
                    "date_time_create",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("date_time_update", models.DateTimeField(auto_now=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("Approve", "Approve"),
                            ("Delivery", "Delivery"),
                            ("Close", "Close"),
                        ],
                        default="New",
                        max_length=10,
                    ),
                ),
                ("order_num", models.UUIDField(null=True, unique=True)),
                (
                    "products",
                    models.ManyToManyField(
                        blank=True, related_name="products", to="shop.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]
