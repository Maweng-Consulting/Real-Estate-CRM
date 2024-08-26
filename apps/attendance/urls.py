from django.urls import path
from apps.attendance.views import visitors, new_visitor, checkout_visitor

urlpatterns = [
    path("visitors/", visitors, name="visitors"),
    path("new-visitor/", new_visitor, name="new-visitor"),
    path("checkout-visitor/", checkout_visitor, name="checkout-visitor"),
]
