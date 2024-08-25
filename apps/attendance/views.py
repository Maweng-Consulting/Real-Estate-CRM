from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q
from decimal import Decimal
from datetime import datetime

from apps.attendance.models import Visitor
# Create your views here.

@login_required(login_url="/users/login")
def visitors(request):
    visitors = Visitor.objects.all().order_by("-created")

    if request.method == "POST":
        id_number = request.POST.get("id_number")
        visitors = Visitor.objects.filter(
            Q(id_number__icontains=id_number)
        ).order_by("-created")

    paginator = Paginator(visitors, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
      
    }
    return render(request, "attendance/visitors/visitors.html", context)


@login_required(login_url="/users/login")
def new_visitor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        id_number = request.POST.get("id_number")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        reason = request.POST.get("reason")
        represents = request.POST.get("represents")

        Visitor.objects.create(
            name=name,
            id_number=id_number,
            email=email,
            phone_number=phone_number,
            gender=gender,
            reason=reason,
            represents=represents
        )
        return redirect("visitors")
    return render(request, "attendance/visitors/new_visitor.html")

@login_required(login_url="/users/login")
def checkout_visitor(request):
    if request.method == "POST":
        visitor_id = request.POST.get("visitor_id")
        visitor = Visitor.objects.get(id=visitor_id)
        visitor.checkout_time = datetime.now()
        visitor.save()
        return redirect("visitors")
    return render(request, "attendance/visitors/checkout_visitor.html")