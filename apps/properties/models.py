from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
PROPERTY_TYPES = (
    ("Land", "Land"),
    ("Building", "Building"),
)

UNIT_STATUSES = (
    ("Booked", "Booked"),
    ("Reserved", "Reserved"),
    ("Sold", "Sold"),
    ("Available", "Available"),
)

class Property(AbstractBaseModel):
    name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=255)
    town = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    total_units = models.IntegerField(default=1)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to="property_images/", null=True)
    title_deed = models.FileField(upload_to="property_title_deeds/", null=True)
    sold_out = models.BooleanField(default=False)
    booking_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    deposit_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
class PropertyPaymentPlan(AbstractBaseModel):
    name = models.CharField(max_length=255)
    payment_period = models.IntegerField(default=1)
    booking_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    deposit_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    installment = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name

    
class PropertyUnit(AbstractBaseModel):
    unit_number = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="propertyunits")
    client = models.ForeignKey("users.Client", on_delete=models.SET_NULL, null=True)
    cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    booking_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    deposit_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    unit_status = models.CharField(max_length=255, choices=UNIT_STATUSES, default="Available")

    def __str__(self):
        return self.unit_number