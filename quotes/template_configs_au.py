from typing import Any, Dict, List, Tuple

from core.choices import Branch, TemplateCode

HeaderField = Dict[str, str]
ChargeColumn = Dict[str, str]
ChargeRow = Dict[str, str]
TemplateConfig = Dict[str, Any]

COMMON_HEADER_FIELDS_AU: List[HeaderField] = [
    {"key": "customer", "label": "Customer"},
    {"key": "issue_date", "label": "Issue Date"},
    {"key": "expiry_date", "label": "Expiry Date"},
    {"key": "attention_to", "label": "Attention To"},
    {"key": "issued_by", "label": "Issued By"},
]


def build_au_title(template_code: str, mode: str) -> str:
    mapping = {
        TemplateCode.IMP_LCL: ("Import LCL", "Seafreight"),
        TemplateCode.IMP_FCL: ("Import FCL", "Seafreight"),
        TemplateCode.EXP_LCL: ("Export LCL", "Seafreight"),
        TemplateCode.EXP_FCL: ("Export FCL", "Seafreight"),
        TemplateCode.EXP_AIR: ("Export", "Airfreight"),
    }
    main, transport = mapping.get(template_code, (template_code, mode))
    return f"{main} {transport} Quotation" if transport else f"{main} Quotation"


AU_QUOTE_TEMPLATES: Dict[str, TemplateConfig] = {
    TemplateCode.IMP_LCL: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.IMP_LCL, mode="Seafreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "ORIGIN_CFS_HANDLING", "label": "Origin CFS Handling"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "OCEAN_FREIGHT", "label": "Ocean Freight"},
                ],
            },
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DEST_PORT_SERVICE", "label": "Destination Port Service"},
                    {"key": "DEST_DELIVERY_ORDER", "label": "Destination Delivery Order"},
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
        ],
    },
    TemplateCode.IMP_AIR: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.IMP_AIR, mode="Airfreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "SECURITY_FEE", "label": "Security Fee"},
                    {"key": "TERMINAL_FEE", "label": "Terminal/Handling Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "AIR_FREIGHT", "label": "Air Freight"},
                    {"key": "FUEL_SURCHARGE", "label": "Fuel Surcharge"},
                ],
            },
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
        ],
    },
    TemplateCode.IMP_FCL: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.IMP_FCL, mode="Seafreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "ORIGIN_TERMINAL", "label": "Origin Terminal Handling"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "OCEAN_FREIGHT", "label": "Ocean Freight"},
                ],
            },
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DEST_PORT_SERVICE", "label": "Destination Port Service"},
                    {"key": "DEST_DELIVERY_ORDER", "label": "Destination Delivery Order"},
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
        ],
    },
    TemplateCode.EXP_LCL: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.EXP_LCL, mode="Seafreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "ORIGIN_CFS_HANDLING", "label": "Origin CFS Handling"},
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "OCEAN_FREIGHT", "label": "Ocean Freight"},
                    {"key": "BUNKER_ADJ", "label": "Bunker Adjustment"},
                ],
            },
        ],
    },
    TemplateCode.EXP_FCL: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.EXP_FCL, mode="Seafreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "ORIGIN_TERMINAL", "label": "Origin Terminal Handling"},
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "OCEAN_FREIGHT", "label": "Ocean Freight"},
                    {"key": "BUNKER_ADJ", "label": "Bunker Adjustment"},
                ],
            },
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DEST_CHARGES", "label": "Destination Charges"},
                ],
            },
        ],
    },
    TemplateCode.EXP_AIR: {
        "branch": Branch.AUSTRALIA,
        "title": build_au_title(TemplateCode.EXP_AIR, mode="Airfreight"),
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
            {"key": "validity_date", "label": "Validity Date"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "HANDLING_FEE", "label": "Handling Fee"},
                    {"key": "SECURITY_FEE", "label": "Security Fee"},
                    {"key": "DOCUMENTATION_FEE", "label": "Documentation Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "AIR_FREIGHT", "label": "Air Freight"},
                    {"key": "FUEL_SURCHARGE", "label": "Fuel Surcharge"},
                ],
            },
        ],
    },
    TemplateCode.AGENT_IMP_FCL: {
        "branch": Branch.AUSTRALIA,
        "title": "Agent Import FCL Charge",
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DEST_PORT_SERVICE", "label": "Destination Port Service"},
                    {"key": "DO_FEE", "label": "Delivery Order Fee"},
                    {"key": "DEST_TRUCKING", "label": "Destination Trucking"},
                    {"key": "OTHER_SURCHARGES", "label": "Other Surcharges"},
                ],
            },
        ],
    },
    TemplateCode.AGENT_IMP_LCL_DAP: {
        "branch": Branch.AUSTRALIA,
        "title": "Agent Import LCL DAP Charge",
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Destination Charges",
                "rows": [
                    {"key": "DEST_CFS", "label": "Destination CFS Handling"},
                    {"key": "DO_FEE", "label": "Delivery Order Fee"},
                    {"key": "DEST_TRUCKING", "label": "Destination Trucking"},
                    {"key": "OTHER_SURCHARGES", "label": "Other Surcharges"},
                ],
            },
        ],
    },
    TemplateCode.AGENT_EXP_LCL_EXW: {
        "branch": Branch.AUSTRALIA,
        "title": "Agent Export LCL EXW Charge",
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "TRUCKING", "label": "Pickup/Trucking"},
                    {"key": "ORIGIN_CFS_HANDLING", "label": "Origin CFS Handling"},
                    {"key": "DOC_FEE", "label": "Documentation Fee"},
                    {"key": "PORT_CHARGES", "label": "Port Charges"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [],
            },
        ],
    },
    TemplateCode.AGENT_EXP_AIR_EXW: {
        "branch": Branch.AUSTRALIA,
        "title": "Agent Export Air EXW Charge",
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "TRUCKING", "label": "Pickup/Trucking"},
                    {"key": "HANDLING_FEE", "label": "Handling Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "AIR_FREIGHT", "label": "Air Freight"},
                    {"key": "FUEL_SURCHARGE", "label": "Fuel Surcharge"},
                ],
            },
        ],
    },
    TemplateCode.AGENT_EXP_FCL: {
        "branch": Branch.AUSTRALIA,
        "title": "Agent Export FCL Charge",
        "header_fields": COMMON_HEADER_FIELDS_AU
        + [
            {"key": "origin", "label": "Origin"},
            {"key": "destination", "label": "Destination"},
            {"key": "incoterm", "label": "Incoterm"},
        ],
        "charge_columns": [
            {"key": "description", "label": "Charge Item"},
            {"key": "currency", "label": "Currency"},
            {"key": "unit", "label": "Unit"},
            {"key": "rate", "label": "Rate"},
            {"key": "min", "label": "Minimum"},
        ],
        "charge_sections": [
            {
                "title": "Origin Charges",
                "rows": [
                    {"key": "TRUCKING", "label": "Pickup/Trucking"},
                    {"key": "ORIGIN_TERMINAL", "label": "Origin Terminal Handling"},
                    {"key": "DOC_FEE", "label": "Documentation Fee"},
                ],
            },
            {
                "title": "Freight Charges",
                "rows": [
                    {"key": "OCEAN_FREIGHT", "label": "Ocean Freight"},
                ],
            },
        ],
    },
}


def get_au_template(code: str) -> TemplateConfig:
    return AU_QUOTE_TEMPLATES[code]


def get_au_template_choices() -> List[Tuple[str, str]]:
    return [(code, cfg["title"]) for code, cfg in AU_QUOTE_TEMPLATES.items()]
