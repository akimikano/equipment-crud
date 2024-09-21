from dataclasses import dataclass
from typing import Optional


@dataclass
class EquipmentAlertEntity:
    id: Optional[int]
    alert_type: str
    message: str
    equipment_id: int
