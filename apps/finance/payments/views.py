from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q
from decimal import Decimal

from apps.finance.models import ClientPayment, ClientInstallment
from apps.users.models import Client

PAYMENT_REASONS = ["Deposit", "Booking", "Installment", "Combined"]
PAYMENT_METHODS = ["Mpesa", "Bank Transfer", "Bank Deposit", "Cash", "Cheque"]


@login_required(login_url="/users/login")
def payments(request):
    payments = ClientPayment.objects.all().order_by("-created")

    clients = Client.objects.all()

    if request.method == "POST":
        id_number = request.POST.get("id_number")
        payments = ClientPayment.objects.filter(
            Q(client__id_number__icontains=id_number)
        )

    paginator = Paginator(payments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "payment_methods": PAYMENT_METHODS,
        "payment_reasons": PAYMENT_REASONS,
        "clients": clients,
    }

    return render(request, "finance/payments/payments.html", context)


@login_required(login_url="/users/login")
def new_payment(request):
    user = request.user
    if request.method == "POST":
        client = request.POST.get("client")
        amount = Decimal(request.POST.get("amount"))
        payment_reason = request.POST.get("payment_reason")
        payment_method = request.POST.get("payment_method")
        date_paid = request.POST.get("date_paid")

        ClientPayment.objects.create(
            client_id=client,
            amount=amount,
            payment_reason=payment_reason,
            recorded_by=user,
            payment_method=payment_method,
            date_paid=date_paid,
        )

        return redirect("payments")
    return render(request, "finance/payments/new_payment.html")


@login_required(login_url="/users/login")
def pay_installment(request):
    user = request.user
    if request.method == "POST":
        installment_id = request.POST.get("installment")
        amount = Decimal(request.POST.get("amount"))
        payment_reason = request.POST.get("payment_reason")
        payment_method = request.POST.get("payment_method")
        date_paid = request.POST.get("date_paid")

        installment = ClientInstallment.objects.get(id=installment_id)

        ClientPayment.objects.create(
            installment=installment,
            amount=amount,
            payment_method=payment_method,
            payment_reason=payment_reason,
            date_paid=date_paid,
            client=installment.client,
            recorded_by=user,
        )

        if amount < installment.amount_expected:
            installment.amount_paid += amount
            installment.status = "Pending"
            installment.save()
        elif amount == installment.amount_expected:
            installment.amount_paid = amount
            installment.status = "Paid"
            installment.paid = True
            installment.save()
        return redirect("installments")

    return render(request, "finance/payments/pay_installment.html")
