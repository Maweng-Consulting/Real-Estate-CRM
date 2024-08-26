from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q


from apps.users.models import Client, User


@login_required(login_url="/users/login/")
def clients(request):
    clients = Client.objects.all().order_by("-created")
    users = User.objects.filter(role="Sales Agent").order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        clients = Client.objects.filter(
            Q(id_number__icontains=search_text) | Q(name__icontains=search_text)
        )

    paginator = Paginator(clients, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "users": users}

    return render(request, "clients/clients.html", context)


@login_required(login_url="/users/login/")
def client_details(request, id):
    client = Client.objects.get(id=id)
    plans = client.clientpaymentplans.all().order_by("-created")
    units = client.clientunits.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        plans = client.clientpaymentplans.filter(
            Q(unit__unit_number__icontains=search_text)
        ).order_by("-created")

    context = {"client": client, "plans": plans, "units": units}
    return render(request, "clients/client_details.html", context)


@login_required(login_url="/users/login/")
def new_client(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone_number")
        id_number = request.POST.get("id_number")
        kra_pin = request.POST.get("kra_pin")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        acquired_by = request.POST.get("acquired_by")

        kra_certificate = request.FILES.get("kra_certificate")
        photo = request.FILES.get("photo")
        id_copy = request.FILES.get("id_copy")

        Client.objects.create(
            name=name,
            email=email,
            gender=gender,
            phone_number=phone_number,
            id_number=id_number,
            kra_pin=kra_pin,
            acquired_by_id=acquired_by,
            kra_certificate=kra_certificate,
            photo=photo,
            id_copy=id_copy,
            address=address,
            city=city,
            country=country,
        )

        return redirect("clients")

    return render(request, "clients/new_client.html")


@login_required(login_url="/users/login/")
def edit_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        email = request.POST.get("email")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone_number")
        id_number = request.POST.get("id_number")
        kra_pin = request.POST.get("kra_pin")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        acquired_by = request.POST.get("acquired_by")

        kra_certificate = request.FILES.get("kra_certificate")
        photo = request.FILES.get("photo")
        id_copy = request.FILES.get("id_copy")

        client = Client.objects.get(id=client_id)
        client.name = name if name else client.name
        client.email = email if email else client.email
        client.gender = gender if gender else client.gender
        client.phone_number = phone_number if phone_number else client.phone_number
        client.id_number = id_number if id_number else client.id_number
        client.kra_pin = kra_pin if kra_pin else client.kra_pin
        client.address = address if address else client.address
        client.city = city if city else client.city
        client.country = country if country else client.country
        client.kra_certificate = (
            kra_certificate if kra_certificate else client.kra_certificate
        )
        client.id_copy = id_copy if id_copy else client.id_copy
        client.photo = photo if photo else client.photo
        client.acquired_by_id = acquired_by
        client.save()

        return redirect("clients")

    return render(request, "clients/edit_client.html")


@login_required(login_url="/users/login/")
def delete_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        client = Client.objects.get(id=client_id)
        client.delete()
        return redirect("clients")
    return render(request, "clients/delete_client.html")
