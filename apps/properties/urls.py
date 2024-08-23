from django.urls import path
from apps.properties.views import properties, new_property, edit_property, delete_property, property_details
from apps.properties.units.views import new_unit, edit_unit, delete_unit, units, assign_unit

urlpatterns = [
    path("", properties, name="properties"),
    path("<int:id>/", property_details, name="property-details"),
    path("new-property/", new_property, name="new-property"),
    path("edit-property/", edit_property, name="edit-property"),
    path("delete-property/", delete_property, name="delete-property"),

    path("<int:id>/units/", units, name="units"),
    path("new-unit/", new_unit, name="new-unit"),
    path("edit-unit/", edit_unit, name="edit-unit"),
    path("assign-unit/", assign_unit, name="assign-unit"),
    path("delete-unit/", delete_unit, name="delete-unit"),
]