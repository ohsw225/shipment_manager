from django.conf import settings
from django.db import models

from core.choices import Branch, CustomerType, ShipmentStatus, TemplateCode


class Shipment(models.Model):
    number = models.CharField(max_length=50, unique=True, blank=True)
    branch = models.CharField(max_length=2, choices=Branch.choices)
    status = models.CharField(
        max_length=20,
        choices=ShipmentStatus.choices,
        default=ShipmentStatus.DRAFT,
    )
    quoted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="shipments",
    )
    customer_name = models.CharField(max_length=255)
    customer_type = models.CharField(
        max_length=20,
        choices=CustomerType.choices,
        default=CustomerType.DIRECT,
    )
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    incoterm = models.CharField(max_length=20)
    shipment_type = models.CharField(max_length=20)
    shipment_date = models.DateField(null=True, blank=True)
    template_code = models.CharField(max_length=30, choices=TemplateCode.choices)
    quote_json = models.JSONField(default=dict, blank=True)
    quote_pdf = models.FileField(upload_to="quotes/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        number = self.number or "Unnumbered"
        return f"{number} - {self.customer_name}"
