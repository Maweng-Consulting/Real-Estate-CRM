from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q

from apps.users.models import Client
from apps.properties.models import PropertyUnit, Property

UNIT_STATUSES = ["Booked", "Reserved", "Sold", "Available"]


@login_required(login_url="/users/login")
def units(request, id):
    property = Property.objects.get(id=id)

    clients = Client.objects.all()

    units = PropertyUnit.objects.filter(property=property).order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        units = (
            PropertyUnit.objects.filter(property=property)
            .filter(Q(unit_number__icontains=search_text))
            .order_by("-created")
        )

    paginator = Paginator(units, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "property": property,
        "page_obj": page_obj,
        "unit_statuses": UNIT_STATUSES,
        "clients": clients,
    }
    return render(request, "properties/units/units.html", context)


@login_required(login_url="/users/login")
def new_unit(request):
    if request.method == "POST":
        property_id = request.POST.get("property_id")
        unit_number = request.POST.get("unit_number")
        cost = request.POST.get("cost")
        unit_status = request.POST.get("unit_status")

        property = Property.objects.get(id=property_id)
        PropertyUnit.objects.create(
            property=property,
            unit_number=unit_number,
            cost=cost,
            unit_status=unit_status,
            booking_fee=property.booking_fee,
            deposit_fee=property.deposit_fee,
        )

        return redirect(f"/properties/{property_id}/units")

    return render(request, "properties/units/new_unit.html")


@login_required(login_url="/users/login")
def edit_unit(request):
    if request.method == "POST":
        unit_id = request.POST.get("unit_id")
        unit_number = request.POST.get("unit_number")
        cost = request.POST.get("cost")
        unit_status = request.POST.get("unit_status")

        unit = PropertyUnit.objects.get(id=unit_id)
        unit.unit_status = unit_status
        unit.unit_number = unit_number
        unit.cost = cost
        unit.save()
        return redirect(f"/properties/{unit.property.id}/units")
    return render(request, "properties/units/edit_unit.html")


@login_required(login_url="/users/login")
def delete_unit(request):
    if request.method == "POST":
        unit_id = request.POST.get("unit_id")
        unit = PropertyUnit.objects.get(id=unit_id)
        unit.delete()
        return redirect(f"/properties/{unit.property.id}/units")
    return render(request, "properties/units/delete_unit.html")


@login_required(login_url="/users/login")
def assign_unit(request):
    if request.method == "POST":
        unit_id = request.POST.get("unit_id")
        client_id = request.POST.get("client_id")
        unit = PropertyUnit.objects.get(id=unit_id)
        client = Client.objects.get(id=client_id)
        unit.client = client
        unit.unit_status = "Booked"
        unit.sold_by = client.acquired_by
        unit.save()
        return redirect(f"/properties/{unit.property.id}/units")
    return render(request, "properties/units/delete_unit.html")
