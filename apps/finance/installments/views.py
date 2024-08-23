from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q

from apps.finance.models import ClientInstallment

INSTALLMENT_STATUSES = ["Paid", "Pending", "Defaulted", "Future"]

@login_required(login_url="/users/login")
def installments(request):
    installments = ClientInstallment.objects.all().order_by("-created")
    if request.method == "POST":
        id_number = request.POST.get("search_text")
        installments = ClientInstallment.objects.filter(Q(client__id_number__icontains=id_number))

    paginator = Paginator(installments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "installment_statuses": INSTALLMENT_STATUSES}

    return render(request, "finance/installments/installments.html", context)


@login_required(login_url="/users/login")
def mark_installment(request):
    if request.method == "POST":
        installment_id = request.POST.get("installment_id")
        action_type = request.POST.get("action_type")

        installment = ClientInstallment.objects.get(id=installment_id)
        installment.status = action_type
        installment.save()

        return redirect("installments")
    return render(request, "finance/installments/mark_installment.html")


@login_required(login_url="/users/login")
def delete_installment(request):
    if request.method == "POST":
        installment_id = request.POST.get("installment_id")
        installment = ClientInstallment.objects.get(id=installment_id)
        installment.delete()
        return redirect("installments")
    return render(request, "finance/installments/delete_installment.html")