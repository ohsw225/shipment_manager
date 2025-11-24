import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from core.choices import Branch, TemplateCode

HeaderField = Dict[str, str]
ChargeColumn = Dict[str, str]
ChargeRow = Dict[str, str]
TemplateConfig = Dict[str, Any]

DATA_PATH = Path(__file__).resolve().parent.parent / "data.json"

SECTION_LABELS: Dict[str, str] = {
    "origin_charges": "Origin Charges",
    "freight_charges": "Freight Charges",
    "destination_charges": "Destination Charges",
    "other_charges": "Other Charges",
}

TEMPLATE_NAME_TO_CODE: Dict[str, str] = {
    "IMP LCL": TemplateCode.IMP_LCL,
    "IMP AIR": TemplateCode.IMP_AIR,
    "IMP FCL": TemplateCode.IMP_FCL,
    "EXP LCL": TemplateCode.EXP_LCL,
    "EXP FCL": TemplateCode.EXP_FCL,
    "EXP AIR": TemplateCode.EXP_AIR,
    "AGENT EXP FCL": TemplateCode.AGENT_EXP_FCL,
    "AGENT IMP FCL": TemplateCode.AGENT_IMP_FCL,
    "AGENT IMP LCL DAP CHARGE": TemplateCode.AGENT_IMP_LCL_DAP,
    "AGENT EXP LCL EXW CHARGE": TemplateCode.AGENT_EXP_LCL_EXW,
    "AGENT EXP AIR EXW CHARGE": TemplateCode.AGENT_EXP_AIR_EXW,
}

TITLE_OVERRIDES: Dict[str, str] = {
    TemplateCode.AGENT_EXP_FCL: "Agent Export FCL Charge",
    TemplateCode.AGENT_IMP_FCL: "Agent Import FCL Charge",
    TemplateCode.AGENT_IMP_LCL_DAP: "Agent Import LCL DAP Charge",
    TemplateCode.AGENT_EXP_LCL_EXW: "Agent Export LCL EXW Charge",
    TemplateCode.AGENT_EXP_AIR_EXW: "Agent Export Air EXW Charge",
}

CODE_MODE: Dict[str, str] = {
    TemplateCode.IMP_LCL: "Seafreight",
    TemplateCode.IMP_AIR: "Airfreight",
    TemplateCode.IMP_FCL: "Seafreight",
    TemplateCode.EXP_LCL: "Seafreight",
    TemplateCode.EXP_FCL: "Seafreight",
    TemplateCode.EXP_AIR: "Airfreight",
}


def build_au_title(template_code: str, mode: str) -> str:
    mapping = {
        TemplateCode.IMP_LCL: ("Import LCL", "Seafreight"),
        TemplateCode.IMP_AIR: ("Import", "Airfreight"),
        TemplateCode.IMP_FCL: ("Import FCL", "Seafreight"),
        TemplateCode.EXP_LCL: ("Export LCL", "Seafreight"),
        TemplateCode.EXP_FCL: ("Export FCL", "Seafreight"),
        TemplateCode.EXP_AIR: ("Export", "Airfreight"),
    }
    main, transport = mapping.get(template_code, (template_code, mode))
    return f"{main} {transport} Quotation" if transport else f"{main} Quotation"


def normalize_key(label: str) -> str:
    """Convert arbitrary labels to stable snake-like keys."""
    key = re.sub(r"[^a-zA-Z0-9]+", "_", label).strip("_").lower()
    return key or "field"


def load_template_payload() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Template data file not found: {DATA_PATH}")
    return json.loads(DATA_PATH.read_text())


def build_header_fields(template: Dict[str, Any]) -> List[HeaderField]:
    fields: List[HeaderField] = []
    seen: set[str] = set()
    for group in ("header_info", "shipment_details"):
        for label in template.get(group, {}).keys():
            key = normalize_key(label)
            if key in seen:
                continue
            fields.append({"key": key, "label": label})
            seen.add(key)
    return fields


def build_charge_columns(template: Dict[str, Any]) -> List[ChargeColumn]:
    columns: List[ChargeColumn] = [{"key": "description", "label": "Charge Item"}]
    seen = {"description"}
    for section in SECTION_LABELS.keys():
        for fields in template.get(section, {}).values():
            for label in fields.keys():
                key = normalize_key(label)
                if key in seen:
                    continue
                columns.append({"key": key, "label": label})
                seen.add(key)
    return columns


def build_charge_sections(template: Dict[str, Any]) -> List[Dict[str, Any]]:
    sections: List[Dict[str, Any]] = []
    for section_key, section_label in SECTION_LABELS.items():
        charges = template.get(section_key, {})
        rows: List[ChargeRow] = [
            {"key": normalize_key(name), "label": name} for name in charges.keys()
        ]
        sections.append({"title": section_label, "rows": rows})
    return sections


def resolve_title(template_code: str, template_name: str) -> str:
    if template_code in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[template_code]
    return build_au_title(template_code, CODE_MODE.get(template_code, ""))


def build_template_config(template: Dict[str, Any]) -> TemplateConfig:
    template_name = template["template_name"]
    template_code = TEMPLATE_NAME_TO_CODE.get(template_name)
    if not template_code:
        raise KeyError(f"Unknown template name in data.json: {template_name}")

    return {
        "branch": Branch.AUSTRALIA,
        "title": resolve_title(template_code, template_name),
        "header_fields": build_header_fields(template),
        "charge_columns": build_charge_columns(template),
        "charge_sections": build_charge_sections(template),
    }


def build_au_templates_from_json() -> Dict[str, TemplateConfig]:
    templates: Dict[str, TemplateConfig] = {}
    for template in load_template_payload():
        config = build_template_config(template)
        templates[TEMPLATE_NAME_TO_CODE[template["template_name"]]] = config

    missing = set(TEMPLATE_NAME_TO_CODE.values()) - set(templates.keys())
    if missing:
        raise ValueError(f"Missing templates in data.json: {sorted(missing)}")
    return templates


AU_QUOTE_TEMPLATES: Dict[str, TemplateConfig] = build_au_templates_from_json()


def get_au_template(code: str) -> TemplateConfig:
    return AU_QUOTE_TEMPLATES[code]


def get_au_template_choices() -> List[Tuple[str, str]]:
    return [(code, cfg["title"]) for code, cfg in AU_QUOTE_TEMPLATES.items()]
