from django.db import models
from apps.core.models import AbstractBaseModel


# Create your models here.
class Visitor(AbstractBaseModel):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    represents = models.CharField(max_length=255, null=True)
    checkout_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
