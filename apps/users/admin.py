from django.contrib import admin
from apps.users.models import User, Client

# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "role"]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone_number"]