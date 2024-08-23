from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q

from apps.users.models import User, Client

# Create your views here.
def people_home(request):
    staff_count = User.objects.exclude(
        role__in=["Supplier", "Broker", "Customer"]
    ).count()
    clients_count = Client.objects.count()

    context = {"staff_count": staff_count, "clients_count": clients_count}
    return render(request, "accounts/home.html", context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["user_id"] = user.id

            login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html")


@login_required(login_url="/users/login/")
def user_logout(request):
    logout(request)
    return redirect("home")
