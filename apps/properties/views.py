from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q

from apps.properties.models import Property, PropertyPaymentPlan, PropertyUnit

PROPERTY_TYPES = ["Building", "Land"]
UNIT_STATUSES = ["Booked", "Reserved", "Sold", "Available"]


@login_required(login_url="/users/login/")
def properties(request):
    properties = Property.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        properties = Property.objects.filter(Q(name__icontains=search_text))

    paginator = Paginator(properties, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "property_types": PROPERTY_TYPES,
        "unit_statuses": UNIT_STATUSES,
    }
    return render(request, "properties/properties.html", context)


@login_required(login_url="/users/login/")
def property_details(request, id):
    property = Property.objects.get(id=id)

    units = property.propertyunits.all()
    paginator = Paginator(units, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "property": property,
        "page_obj": page_obj,
        "unit_statuses": UNIT_STATUSES,
    }
    return render(request, "properties/property_details.html", context)


@login_required(login_url="/users/login/")
def new_property(request):
    if request.method == "POST":
        name = request.POST.get("name")
        property_type = request.POST.get("property_type")
        location = request.POST.get("location")
        town = request.POST.get("town")
        county = request.POST.get("county")
        total_units = request.POST.get("total_units")
        total_cost = request.POST.get("total_cost")
        booking_fee = request.POST.get("booking_fee")
        deposit_fee = request.POST.get("deposit_fee")

        image = request.FILES.get("image")
        title_deed = request.FILES.get("title_deed")

        Property.objects.create(
            name=name,
            property_type=property_type,
            location=location,
            town=town,
            county=county,
            total_units=total_units,
            total_cost=total_cost,
            booking_fee=booking_fee,
            deposit_fee=deposit_fee,
            image=image,
            title_deed=title_deed,
        )

        return redirect("properties")

    return render(request, "properties/new_property.html")


@login_required(login_url="/users/login/")
def edit_property(request):
    if request.method == "POST":
        property_id = request.POST.get("property_id")
        name = request.POST.get("name")
        property_type = request.POST.get("property_type")
        location = request.POST.get("location")
        town = request.POST.get("town")
        county = request.POST.get("county")
        total_units = request.POST.get("total_units")
        total_cost = request.POST.get("total_cost")
        booking_fee = request.POST.get("booking_fee")
        deposit_fee = request.POST.get("deposit_fee")

        image = request.FILES.get("image")
        title_deed = request.FILES.get("title_deed")

        property = Property.objects.get(id=property_id)
        property.name = name if name else property.name
        property.property_type = (
            property_type if property_type else property.property_type
        )
        property.location = location if location else property.location
        property.town = town if town else property.town
        property.county = county if county else property.county
        property.total_cost = total_cost if total_cost else property.total_cost
        property.total_units = total_units if total_units else property.total_units
        property.booking_fee = booking_fee if booking_fee else property.booking_fee
        property.deposit_fee = deposit_fee if deposit_fee else property.deposit_fee
        property.image = image if image else property.image
        property.title_deed = title_deed if title_deed else property.title_deed
        property.save()

        return redirect("properties")

    return render(request, "properties/edit_property.html")


@login_required(login_url="/users/login/")
def delete_property(request):
    if request.method == "POST":
        property_id = request.POST.get("property_id")
        property = Property.objects.get(id=property_id)
        property.delete()
        return redirect("properties")
    return render(request, "properties/delete_property.html")
