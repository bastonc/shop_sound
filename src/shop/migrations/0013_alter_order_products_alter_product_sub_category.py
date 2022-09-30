# Generated by Django 4.1.1 on 2022-09-29 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_brand_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='shop.subcategory'),
        ),
    ]
