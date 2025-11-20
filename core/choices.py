from django.db import models


class Branch(models.TextChoices):
    KOREA = "KR", "Korea"
    AUSTRALIA = "AU", "Australia"


class ShipmentStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    WAITING = "WAITING", "Waiting"
    BOOKED = "BOOKED", "Booked"
    IN_TRANSIT = "IN_TRANSIT", "In transit"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"


class CustomerType(models.TextChoices):
    DIRECT = "DIRECT", "Direct Customer"
    AGENT = "AGENT", "Overseas Agent"
    OTHER = "OTHER", "Other"


class TemplateCode(models.TextChoices):
    IMP_LCL = "IMP_LCL", "Import LCL"
    IMP_AIR = "IMP_AIR", "Import Air"
    IMP_FCL = "IMP_FCL", "Import FCL"
    EXP_LCL = "EXP_LCL", "Export LCL"
    EXP_FCL = "EXP_FCL", "Export FCL"
    EXP_AIR = "EXP_AIR", "Export Air"
    AGENT_EXP_FCL = "AGENT_EXP_FCL", "Agent Export FCL"
    AGENT_IMP_FCL_DAP = "AGENT_IMP_FCL_DAP", "Agent Import FCL DAP"
    AGENT_IMP_LCL_DAP = "AGENT_IMP_LCL_DAP", "Agent Import LCL DAP"
    AGENT_EXP_LCL_EXW = "AGENT_EXP_LCL_EXW", "Agent Export LCL EXW"
    AGENT_EXP_AIR_EXW = "AGENT_EXP_AIR_EXW", "Agent Export Air EXW"
