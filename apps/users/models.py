from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import AbstractBaseModel

# Create your models here.
ROLE_CHOICES = (
    ("Admin", "Admin"),
    ("Receptionist", "Receptionist"),
    ("Sales Agent", "Sales Agent"),
    ("Finance Admin", "Finance Admin"),
    ("HRM Admin", "HRM Admin"),
)


class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    kra_pin = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username

    def name(self):
        if not self.first_name and self.last_name:
            return self.username
        else:
            return f"{self.first_name} {self.last_name}"


class Client(AbstractBaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    kra_pin = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    id_copy = models.FileField(upload_to="client_ids/", null=True)
    kra_certificate = models.FileField(upload_to="kra_cerificates/", null=True)
    photo = models.ImageField(upload_to="client_photos/", null=True)

    def __str__(self):
        return self.name


class NextOfKin(AbstractBaseModel):
    employee = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="nextofkins"
    )
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    relation = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
