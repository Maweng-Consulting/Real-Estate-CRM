from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q
from apps.users.models import User

USER_ROLES = ["Admin", "Receptionist", "Sales Agent", "Finance Admin", "HRM Admin"]

def staff(request):
    employees = User.objects.all().order_by("-created")

    if request.method == "POST":
        id_number = request.POST.get("id_number")
        employees = User.objects.filter(id_number=id_number)

    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "user_roles": USER_ROLES}

    return render(request, "staff/staff.html", context)

@login_required(login_url="/users/login/")
def new_staff(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        role = request.POST.get("role")
        phone_number = request.POST.get("phone_number")
        id_number = request.POST.get("id_number")
        position = request.POST.get("position")
        kra_pin = request.POST.get("kra_pin")

        user_by_email = User.objects.filter(email=email).first()
        user_by_id = User.objects.filter(username=id_number).first()

        if user_by_email:
            messages.error(
                request, f"User with this email exists already, try a different email!!"
            )

        elif user_by_id:
            messages.error(
                request,
                f"User with this username exists already, try a different username!!",
            )

            print(email, first_name, last_name)
        else:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=id_number,
                email=email,
                role=role,
                gender=gender,
                phone_number=phone_number,
                id_number=id_number,
                position=position,
                kra_pin=kra_pin
            )
            user.set_password("1234")
            user.save()
            messages.success(request, f"User created successfully!!")

            return redirect("employees")

    return render(request, "staff/new_staff.html")

@login_required(login_url="/users/login/")
def edit_staff(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        if user_id:
            username = request.POST.get("username")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            gender = request.POST.get("gender")
            role = request.POST.get("role")
            phone_number = request.POST.get("phone_number")
            id_number = request.POST.get("id_number")
            position = request.POST.get("position")
            kra_pin = request.POST.get("kra_pin")
            address = request.POST.get("address")
            town = request.POST.get("town")
            country = request.POST.get("country")

            user = User.objects.get(id=user_id)
            user.first_name = first_name if first_name else user.first_name
            user.last_name = last_name if last_name else user.last_name
            user.email = email if email else user.email
            user.gender = gender if gender else user.gender
            user.phone_number = phone_number if phone_number else user.phone_number
            user.id_number = id_number if id_number else user.id_number
            user.username = username if username else user.username
            user.role = role if role else user.role
            user.position = position
            user.kra_pin = kra_pin
            user.address = address
            user.city = town
            user.country = country if country else "Kenya"
            user.save()
            messages.success(request, f"User created successfully!!")

        return redirect("employees")

    return render(request, "staff/edit_staff.html")

@login_required(login_url="/users/login/")
def delete_staff(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        staff = User.objects.filter(id=user_id).first()
        if staff:
            staff.delete()
            return redirect("employees")
        else:
            return messages.error(
                request, f"Staff with id: {user_id} does not exist on the database"
            )
    return render(request, "staff/delete_staff.html")