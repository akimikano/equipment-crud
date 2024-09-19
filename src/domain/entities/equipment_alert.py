from dataclasses import dataclass
from typing import Optional


@dataclass
class EquipmentAlert:
    id: Optional[int]
    alert_type: str
    message: str
    equipment_id: int
