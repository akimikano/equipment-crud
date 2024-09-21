from src.application.exceptions import NotFound
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.application.repositories.equipment_repository import \
    IEquipmentRepository


class UpdateEquipmentUseCase(BaseUseCase):
    def __init__(self, *, equipment_repository: IEquipmentRepository):
        self.equipment_repository = equipment_repository

    async def execute(self, *, equipment_id: int, request_data: dict):
        db_equipment = await self.equipment_repository.fetch_one(
            pk=equipment_id
        )
        if not db_equipment:
            raise NotFound

        equipment = await self.equipment_repository.update_one(
            pk=equipment_id,
            data=request_data
        )
        await self.equipment_repository.save_changes()
        return equipment
