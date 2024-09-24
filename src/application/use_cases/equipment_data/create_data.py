from src.application.repositories.equipment_data_repository import \
    IEquipmentDataRepository
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.equipment_data import EquipmentDataEntity


class CreateEquipmentDataUseCase(BaseUseCase):
    def __init__(self, *, equipment_data_repository: IEquipmentDataRepository):
        self.equipment_data_repository = equipment_data_repository

    async def execute(self, request_data: dict):

        equipment_data = EquipmentDataEntity(
            id=None,
            **request_data
        )

        await self.equipment_data_repository.save_one(entity=equipment_data)
        await self.equipment_data_repository.save_changes()
        return equipment_data
