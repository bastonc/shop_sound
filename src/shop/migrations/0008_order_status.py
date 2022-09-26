# Generated by Django 4.1.1 on 2022-09-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_order_date_time_create_order_date_time_update_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
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
    ]
