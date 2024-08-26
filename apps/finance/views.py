from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.finance.models import ClientPayment, ClientInstallment, ClientPaymentPlan


# Create your views here.
@login_required(login_url="/users/login")
def home(request):
    payment_plans_count = ClientPaymentPlan.objects.count()
    payments_count = ClientPayment.objects.count()
    installments_count = ClientInstallment.objects.count()

    context = {
        "payment_plans_count": payment_plans_count,
        "payments_count": payments_count,
        "installments_count": installments_count,
    }
    return render(request, "finance/home.html", context)


@login_required(login_url="/users/login")
def generate_offer_letter(request, id):
    plan = ClientPaymentPlan.objects.get(id=id)

    context = {"plan": plan}
    return render(request, "documents/offer_letter.html", context)
