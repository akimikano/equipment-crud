from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from src.domain.entities.equipment_alert import EquipmentAlertEntity
from src.domain.entities.equipment_data import EquipmentDataEntity


@dataclass
class EquipmentEntity:
    id: Optional[int]
    equipment_type: str
    model: str
    installed_at: datetime
    status: str
    alerts: List[EquipmentAlertEntity]
    data: List[EquipmentDataEntity]
