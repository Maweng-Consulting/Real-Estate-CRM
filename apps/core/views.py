from django.shortcuts import render
from apps.users.models import User, Client
from apps.properties.models import Property
# Create your views here.
def home(request):
    staff_count = User.objects.count()
    clients_count = Client.objects.count()
    properties_count = Property.objects.count()

    context = {
        "staff_count": staff_count,
        "clients_count": clients_count,
        "properties_count": properties_count
    }
    return render(request, "home.html", context)