from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.domain.enums import EquipmentType, EquipmentStatus, AlertType


class EquipmentAlertBase(BaseModel):
    alert_type: AlertType
    message: str
    equipment_id: int


class EquipmentAlertCreate(EquipmentAlertBase):
    pass


class EquipmentAlertUpdate(EquipmentAlertBase):
    pass


class EquipmentAlertDetail(EquipmentAlertBase):
    id: int


class EquipmentDataBase(BaseModel):
    key: str
    value: str
    equipment_id: int


class EquipmentDataCreate(EquipmentDataBase):
    pass


class EquipmentDataUpdate(EquipmentDataBase):
    pass


class EquipmentDataDetail(EquipmentDataBase):
    id: int


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
    alerts: List[EquipmentAlertDetail]
    data: List[EquipmentDataDetail]
