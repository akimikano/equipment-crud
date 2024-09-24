from src.application.repositories.equipment_data_repository import \
    IEquipmentDataRepository
from src.domain.entities.equipment_data import EquipmentDataEntity
from src.infrastructure.database.sqlalchemy.models import EquipmentDataModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository


class EquipmentDataRepository(BaseAsyncRepository, IEquipmentDataRepository):
    model = EquipmentDataModel

    @staticmethod
    def to_entity(db_instance: EquipmentDataModel):
        return EquipmentDataEntity(
            id=db_instance.id,
            key=db_instance.key,
            value=db_instance.value,
            equipment_id=db_instance.equipment_id
        )
