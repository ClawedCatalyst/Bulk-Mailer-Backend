# Generated by Django 4.1.4 on 2022-12-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_new_user_resgistration_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new_user_resgistration",
            name="mobile",
            field=models.BigIntegerField(blank=True),
        ),
    ]
