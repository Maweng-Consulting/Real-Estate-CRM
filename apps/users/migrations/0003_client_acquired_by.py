# Generated by Django 4.2 on 2024-08-26 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_client_nextofkin"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="acquired_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
