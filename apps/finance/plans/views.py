from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q

from apps.users.models import Client
from apps.properties.models import PropertyUnit
from apps.finance.models import ClientPaymentPlan, ClientInstallment

def payment_plans(request):
    plans = ClientPaymentPlan.objects.all().order_by("-created")

    clients = Client.objects.all().order_by("-created")
    units = PropertyUnit.objects.all().only('id', 'unit_number', 'client_id')
    print(units)

    if request.method == "POST":
        id_number = request.POST.get("id_number")
        plans = ClientPaymentPlan.objects.filter(Q(client__id_number__icontains=id_number))

    paginator = Paginator(plans, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "clients": clients, "units": units}

    return render(request, "finance/payment_plans/plans.html", context)


def payment_plan_details(request, id):
    plan = ClientPaymentPlan.objects.get(id=id)
    installments = ClientInstallment.objects.filter(payment_plan=plan).order_by("-created")

    if request.method == "POST":
        id_number = request.POST.get("search_text")
        installments = ClientInstallment.objects.filter(Q(client__id_number__icontains=id_number))

    paginator = Paginator(installments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "plan": plan}

    return render(request, "finance/payment_plans/plan_details.html", context)


def new_payment_plan(request):
    if request.method == "POST":
        client_id = request.POST.get("client")
        unit_id = request.POST.get("unit")
        booking_fee = request.POST.get("booking_fee")
        deposit_fee = request.POST.get("deposit_fee")
        period = request.POST.get("period")
        installment_amount = request.POST.get("installment_amount")
        total_amount = request.POST.get("total_amount")
        first_installment_date = request.POST.get("first_installment_date")

        ClientPaymentPlan.objects.create(
            client_id=client_id,
            unit_id=unit_id,
            booking_fee=booking_fee,
            deposit_fee=deposit_fee,
            period=period,
            installment_amount=installment_amount,
            total_amount=total_amount,
            first_repayment_date =first_installment_date
        )
        return redirect("payment-plans")
    return render(request, "finance/payment_plans/new_plan.html")


def delete_payment_plan(request):
    if request.method == "POST":
        plan_id = request.POST.get("plan_id")
        payment_plan = ClientPaymentPlan.objects.get(id=plan_id)
        installments = ClientInstallment.objects.filter(payment_plan=payment_plan)
        installments.delete()
        payment_plan.delete()
        return redirect("payment-plans")
    return render(request, "finance/payment_plans/delete_plan.html")