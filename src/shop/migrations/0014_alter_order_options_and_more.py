# Generated by Django 4.1.1 on 2022-11-14 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_product_alias"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ("-created",),
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.RenameField(
            model_name="order",
            old_name="date_time_create",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="date_time_update",
            new_name="updated",
        ),
        migrations.RemoveField(
            model_name="order",
            name="order_num",
        ),
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.RemoveField(
            model_name="order",
            name="user",
        ),
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="city",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="first_name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="last_name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="postal_code",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="shop.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="order_items",
                        to="shop.product",
                    ),
                ),
            ],
        ),
    ]
