from src.application.repositories.equipment_repository import \
    IEquipmentRepository
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.equipment import EquipmentEntity


class CreateEquipmentUseCase(BaseUseCase):
    def __init__(self, *, equipment_repository: IEquipmentRepository):
        self.equipment_repository = equipment_repository

    async def execute(self, request_data: dict):

        equipment = EquipmentEntity(
            id=None,
            **request_data
        )

        await self.equipment_repository.save_one(entity=equipment)
        await self.equipment_repository.save_changes()
        return equipment
