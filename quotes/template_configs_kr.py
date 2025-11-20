from typing import Any, Dict, List, Tuple

from core.choices import Branch, TemplateCode

HeaderField = Dict[str, str]
ChargeColumn = Dict[str, str]
ChargeRow = Dict[str, str]
TemplateConfig = Dict[str, Any]

COMMON_HEADER_FIELDS_KR: List[HeaderField] = [
    {"key": "customer", "label": "Customer"},
    {"key": "issue_date", "label": "Issue Date"},
    {"key": "attention_to", "label": "Attention To"},
    {"key": "issued_by", "label": "Issued By"},
]

COMMON_CHARGE_COLUMNS: List[ChargeColumn] = [
    {"key": "description", "label": "Charge Item"},
    {"key": "currency", "label": "Currency"},
    {"key": "unit", "label": "Unit"},
    {"key": "rate", "label": "Rate"},
    {"key": "min", "label": "Minimum"},
]

KR_QUOTE_TEMPLATES: Dict[str, TemplateConfig] = {
}


def get_kr_template(code: str) -> TemplateConfig:
    return KR_QUOTE_TEMPLATES[code]


def get_kr_template_choices() -> List[Tuple[str, str]]:
    return [(code, cfg["title"]) for code, cfg in KR_QUOTE_TEMPLATES.items()]
