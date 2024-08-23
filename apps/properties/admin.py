from django.contrib import admin
from apps.properties.models import PropertyUnit, PropertyPaymentPlan, Property
# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "total_units", "total_cost", "sold_out"]


@admin.register(PropertyUnit)
class PropertyUnitAdmin(admin.ModelAdmin):
    list_display = ["id", "unit_number", "property", "client", "unit_status"]