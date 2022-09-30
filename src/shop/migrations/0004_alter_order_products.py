# Generated by Django 4.1.1 on 2022-09-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_order_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(null=True, related_name="orders", to="shop.product"),
        ),
    ]