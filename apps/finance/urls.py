from django.urls import path
from apps.finance.views import home, generate_offer_letter
from apps.finance.plans.views import (
    payment_plans,
    new_payment_plan,
    delete_payment_plan,
    payment_plan_details,
)
from apps.finance.installments.views import (
    installments,
    mark_installment,
    delete_installment,
)
from apps.finance.payments.views import payments, new_payment, pay_installment

urlpatterns = [
    path("", home, name="finance"),
    path("generate-offer-letter/<int:id>/", generate_offer_letter, name="generate-offer-letter"),
    # Payment Plans
    path("payment-plans/", payment_plans, name="payment-plans"),
    path(
        "payment-plans/<int:id>/details",
        payment_plan_details,
        name="payment-plan-details",
    ),
    path("new-payment-plan/", new_payment_plan, name="new-payment-plan"),
    path("delete-payment-plan/", delete_payment_plan, name="delete-payment-plan"),
    # Installments
    path("installments/", installments, name="installments"),
    path("mark-installment/", mark_installment, name="mark-installment"),
    path("delete-installment/", delete_installment, name="delete-installment"),
    # Payments
    path("payments/", payments, name="payments"),
    path("new-payment/", new_payment, name="new-payment"),
    path("pay-installment/", pay_installment, name="pay-installment"),
]
