from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, DateTime, Enum, ForeignKey

from src.domain.enums import EquipmentType, EquipmentStatus, AlertType
from src.infrastructure.database.sqlalchemy.models.base_model import Base


class EquipmentModel(Base):
    __tablename__ = "equipments"

    id: Mapped[int] = mapped_column(primary_key=True)
    equipment_type: Mapped[str] = mapped_column(Enum(EquipmentType))
    model: Mapped[str] = mapped_column(String(255))
    installed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(Enum(EquipmentStatus))

    # relationships
    alerts: Mapped[List["EquipmentAlertModel"]] = relationship(
        cascade="all, delete-orphan"
    )
    data: Mapped[List["EquipmentDataModel"]] = relationship(
        cascade="all, delete-orphan"
    )


class EquipmentAlertModel(Base):
    __tablename__ = "equipment_alerts"

    id: Mapped[int] = mapped_column(primary_key=True)
    alert_type: Mapped[str] = mapped_column(Enum(AlertType))
    message: Mapped[str] = mapped_column(String(255))
    equipment_id: Mapped[int] = mapped_column(ForeignKey("equipments.id"))


class EquipmentDataModel(Base):
    __tablename__ = "equipment_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(255))
    value: Mapped[str] = mapped_column(String(255))
    equipment_id: Mapped[int] = mapped_column(ForeignKey("equipments.id"))
