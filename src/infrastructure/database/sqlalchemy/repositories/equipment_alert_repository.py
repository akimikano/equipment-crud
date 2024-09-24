from src.application.repositories.equipment_alert_repository import \
    IEquipmentAlertRepository
from src.domain.entities.equipment_alert import EquipmentAlertEntity
from src.infrastructure.database.sqlalchemy.models import EquipmentAlertModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository


class EquipmentAlertRepository(BaseAsyncRepository, IEquipmentAlertRepository):
    model = EquipmentAlertModel

    @staticmethod
    def to_entity(db_instance: EquipmentAlertModel):
        return EquipmentAlertEntity(
            id=db_instance.id,
            alert_type=db_instance.alert_type,
            message=db_instance.message,
            equipment_id=db_instance.equipment_id
        )
