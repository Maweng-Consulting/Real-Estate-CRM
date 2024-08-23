from django.urls import path
from apps.users.views import user_login, user_logout, people_home
from apps.users.staff.views import staff, new_staff, edit_staff, delete_staff
from apps.users.clients.views import clients, new_client, edit_client, delete_client

urlpatterns = [
    path("", people_home, name="people"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    # Staff
    path("employees/", staff, name="employees"),
    path("new-employee/", new_staff, name="new-employee"),
    path("edit-employee/", edit_staff, name="edit-employee"),
    path("delete-employee/", delete_staff, name="delete-employee"),

    # Clients
    path("clients/", clients, name="clients"),
    path("new-client/", new_client, name="new-client"),
    path("edit-client/", edit_client, name="edit-client"),
    path("delete-client/", delete_client, name="delete-client"),
]