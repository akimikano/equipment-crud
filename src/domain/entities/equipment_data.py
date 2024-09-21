from dataclasses import dataclass
from typing import Optional


@dataclass
class EquipmentDataEntity:
    id: Optional[int]
    key: str
    value: str
    equipment_id: int
