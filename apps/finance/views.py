from django.shortcuts import render

from apps.finance.models import ClientPayment, ClientInstallment, ClientPaymentPlan
# Create your views here.
def home(request):
    payment_plans_count = ClientPaymentPlan.objects.count()
    payments_count = ClientPayment.objects.count()
    installments_count = ClientInstallment.objects.count()

    context = {
        "payment_plans_count": payment_plans_count,
        "payments_count": payments_count,
        "installments_count": installments_count
    }
    return render(request, "finance/home.html", context)