from datetime import datetime

from pydantic import BaseModel

from src.domain.enums import EquipmentType, EquipmentStatus


class EquipmentBase(BaseModel):
    equipment_type: EquipmentType
    model: str
    installed_at: datetime
    status: EquipmentStatus


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(EquipmentBase):
    pass


class EquipmentDetail(EquipmentBase):
    id: int
