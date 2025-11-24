from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Shipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(blank=True, max_length=50, unique=True),
                ),
                (
                    "branch",
                    models.CharField(
                        choices=[("KR", "Korea"), ("AU", "Australia")], max_length=2
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DRAFT", "Draft"),
                            ("WAITING", "Waiting"),
                            ("BOOKED", "Booked"),
                            ("IN_TRANSIT", "In transit"),
                            ("DELIVERED", "Delivered"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="DRAFT",
                        max_length=20,
                    ),
                ),
                (
                    "customer_name",
                    models.CharField(max_length=255),
                ),
                (
                    "customer_type",
                    models.CharField(
                        choices=[
                            ("DIRECT", "Direct Customer"),
                            ("AGENT", "Overseas Agent"),
                            ("OTHER", "Other"),
                        ],
                        default="DIRECT",
                        max_length=20,
                    ),
                ),
                ("origin", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("incoterm", models.CharField(max_length=20)),
                ("shipment_type", models.CharField(max_length=20)),
                (
                    "shipment_date",
                    models.DateField(blank=True, null=True),
                ),
                (
                    "template_code",
                    models.CharField(
                        choices=[
                            ("IMP_LCL", "Import LCL"),
                            ("IMP_AIR", "Import Air"),
                            ("IMP_FCL", "Import FCL"),
                            ("EXP_LCL", "Export LCL"),
                            ("EXP_FCL", "Export FCL"),
                            ("EXP_AIR", "Export Air"),
                            ("AGENT_EXP_FCL", "Agent Export FCL"),
                            ("AGENT_IMP_FCL", "Agent Import FCL"),
                            ("AGENT_IMP_LCL_DAP", "Agent Import LCL DAP Charge"),
                            ("AGENT_EXP_LCL_EXW", "Agent Export LCL EXW Charge"),
                            ("AGENT_EXP_AIR_EXW", "Agent Export Air EXW Charge"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "quote_json",
                    models.JSONField(blank=True, default=dict),
                ),
                (
                    "quote_pdf",
                    models.FileField(blank=True, null=True, upload_to="quotes/"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True),
                ),
                (
                    "quoted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shipments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
