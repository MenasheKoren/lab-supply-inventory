from django.core.validators import MinValueValidator
from django.db import models


class Inventory(models.Model):
    UNIT_CHOICES = {
        "mL": "milliliter",
        "L": "liter",
        "µL": "microliter",
        "g": "gram",
        "mg": "milligram",
        "kg": "kilogram",
        "OTH": "other",
    }
    name = models.CharField(
        max_length=100,
        verbose_name="Item name",
        help_text="Enter the item name",
        error_messages={
            "blank": "Please enter the item name.",
            "null": "Please enter the item name.",
            "max_length": "The item name cannot exceed 100 characters.",
        },
    )
    catalog_number = models.CharField(
        max_length=100,
        verbose_name="Catalog number",
        help_text="Enter the catalog number",
        error_messages={
            "blank": "Please enter the catalog number.",
            "null": "Please enter the catalog number.",
            "max_length": "The catalog number cannot exceed 100 characters.",
        },
    )
    lot_number = models.CharField(
        max_length=100,
        verbose_name="Lot number",
        blank=True,
        null=True,
        help_text="Enter the lot number",
        error_messages={
            "max_length": "The lot number cannot exceed 100 characters.",
        },
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Quantity",
        help_text="Enter the quantity",
        validators=[MinValueValidator(0)],
        error_messages={
            "blank": "Please enter the quantity.",
            "null": "Please enter the quantity.",
        },
    )
    unit = models.CharField(
        choices=UNIT_CHOICES,
        max_length=3,
        default="mL",
        verbose_name="Unit",
        help_text="Select the measurement unit",
    )
    volume = models.FloatField(
        default=0,
        verbose_name="Volume",
        help_text="Enter the volume",
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
        error_messages={
            "blank": "Please enter the volume.",
            "null": "Please enter the volume.",
            "invalid": "Please enter a valid number.",
        },
    )
    expires_on = models.DateField(
        null=True,
        blank=True,
        verbose_name="Expiration date",
        help_text="Enter the expiration date",
    )
    provider = models.CharField(
        max_length=100,
        verbose_name="Provider",
        help_text="Enter the provider",
        error_messages={
            "blank": "Please enter the provider's name.",
            "null": "Please enter the provider's name.",
            "max_length": "The provider's name cannot exceed 100 characters.",
        },
    )
    manufacturer = models.CharField(
        max_length=100,
        verbose_name="Manufacturer",
        help_text="Enter the manufacturer",
        null=True,
        blank=True,
        error_messages={
            "max_length": "The manufacturer's name cannot exceed 100 characters.",
        },
    )
    comments = models.TextField(
        blank=True,
        null=True,
        verbose_name="Comments",
        help_text="Enter any additional comments or notes about the item",
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated on")

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
