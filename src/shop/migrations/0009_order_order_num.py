# Generated by Django 4.1.1 on 2022-09-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_num",
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
    ]
