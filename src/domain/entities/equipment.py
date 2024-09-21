from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EquipmentEntity:
    id: Optional[int]
    equipment_type: str
    model: str
    installed_at: datetime
    status: str
