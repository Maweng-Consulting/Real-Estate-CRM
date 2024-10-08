# Generated by Django 4.2 on 2024-08-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0010_clientpayment_payment_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientpayment",
            name="date_paid",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="clientpayment",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Mpesa", "Mpesa"),
                    ("Bank Transfer", "Bank Transfer"),
                    ("Bank Deposit", "Bank Deposit"),
                    ("Cash", "Cash"),
                    ("Cheque", "Cheque"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
