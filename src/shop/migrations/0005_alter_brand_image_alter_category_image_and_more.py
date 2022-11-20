# Generated by Django 4.1.1 on 2022-10-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_pages_alter_brand_image_alter_category_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="image",
            field=models.ImageField(
                default="static/images/non-image.png",
                null=True,
                upload_to="media/image/products/",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                default="static/images/non-image.png",
                null=True,
                upload_to="media/image/category/",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default="static/images/non-image.png",
                null=True,
                upload_to="media/image/products/",
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="image",
            field=models.ImageField(
                default="static/images/non-image.png",
                null=True,
                upload_to="media/image/sub-category/",
            ),
        ),
    ]