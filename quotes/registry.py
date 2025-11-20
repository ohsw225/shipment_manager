from typing import Dict, List, Tuple

from core.choices import Branch
from .template_configs_au import AU_QUOTE_TEMPLATES, get_au_template_choices
from .template_configs_kr import KR_QUOTE_TEMPLATES, get_kr_template_choices


class TemplateRegistry:
    """Central lookup for template configs per branch/code."""

    def __init__(self) -> None:
        self._templates: Dict[str, Dict[str, dict]] = {
            Branch.AUSTRALIA: AU_QUOTE_TEMPLATES,
            Branch.KOREA: KR_QUOTE_TEMPLATES,
        }

    def get(self, branch: str, code: str) -> dict:
        templates = self._templates.get(branch)
        if templates is None or code not in templates:
            raise KeyError(f"Template not found for branch={branch} code={code}")
        return templates[code]

    def choices(self, branch: str) -> List[Tuple[str, str]]:
        if branch == Branch.AUSTRALIA:
            return get_au_template_choices()
        if branch == Branch.KOREA:
            return get_kr_template_choices()
        return []


def get_registry() -> TemplateRegistry:
    return TemplateRegistry()
