# Generated by Django 4.2 on 2024-08-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitor",
            name="checkout_time",
            field=models.DateTimeField(null=True),
        ),
    ]
