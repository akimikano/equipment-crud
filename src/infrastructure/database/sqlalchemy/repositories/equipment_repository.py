from sqlalchemy import select, desc

from src.domain.entities.equipment import EquipmentEntity
from src.infrastructure.database.sqlalchemy.models import EquipmentModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository
from src.application.repositories.equipment_repository import \
    IEquipmentRepository


class EquipmentRepository(BaseAsyncRepository, IEquipmentRepository):
    model = EquipmentModel

    @staticmethod
    def to_entity(db_instance: EquipmentModel):
        return EquipmentEntity(
            id=db_instance.id,
            equipment_type=db_instance.equipment_type,
            model=db_instance.model,
            installed_at=db_instance.installed_at,
            status=db_instance.status
        )
