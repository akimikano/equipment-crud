from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from src.domain.entities.equipment import EquipmentEntity
from src.domain.entities.equipment_alert import EquipmentAlertEntity
from src.domain.entities.equipment_data import EquipmentDataEntity
from src.infrastructure.database.sqlalchemy.models import EquipmentModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository
from src.application.repositories.equipment_repository import \
    IEquipmentRepository


class EquipmentRepository(BaseAsyncRepository, IEquipmentRepository):
    model = EquipmentModel

    def query(self):
        return (
            select(self.model)
            .options(
                selectinload(self.model.alerts),
                selectinload(self.model.data))
            .order_by(desc(self.model.id)))

    @staticmethod
    def to_entity(db_instance: EquipmentModel):
        return EquipmentEntity(
            id=db_instance.id,
            equipment_type=db_instance.equipment_type,
            model=db_instance.model,
            installed_at=db_instance.installed_at,
            status=db_instance.status,
            alerts=[
                EquipmentAlertEntity(
                    id=alert.id,
                    alert_type=alert.alert_type,
                    message=alert.message,
                    equipment_id=alert.equipment_id
                ) for alert in db_instance.alerts
            ],
            data=[
                EquipmentDataEntity(
                    id=data.id,
                    key=data.key,
                    value=data.value,
                    equipment_id=data.equipment_id
                ) for data in db_instance.data
            ]
        )
