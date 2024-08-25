from django.shortcuts import render
from apps.users.models import User, Client
from apps.properties.models import Property
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/users/login")
def home(request):
    staff_count = User.objects.count()
    clients_count = Client.objects.count()
    properties_count = Property.objects.count()

    context = {
        "staff_count": staff_count,
        "clients_count": clients_count,
        "properties_count": properties_count,
    }
    return render(request, "home.html", context)
