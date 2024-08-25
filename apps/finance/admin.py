from django.contrib import admin
from apps.finance.models import ClientPayment, ClientPaymentPlan, ClientInstallment


# Register your models here.
@admin.register(ClientInstallment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "payment_plan", "amount_expected", "date_expected"]


@admin.register(ClientPaymentPlan)
class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "unit", "total_amount"]
