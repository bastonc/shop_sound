# Generated by Django 4.1.1 on 2022-11-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="images/profiles/user-def.png",
                null=True,
                upload_to="images/profiles/",
            ),
        ),
    ]