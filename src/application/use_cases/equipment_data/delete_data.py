from src.application.repositories.equipment_data_repository import \
    IEquipmentDataRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class DeleteEquipmentDataUseCase(BaseUseCase):
    def __init__(self, *, equipment_data_repository: IEquipmentDataRepository):
        self.equipment_data_repository = equipment_data_repository

    async def execute(self, data_id: int):
        await self.equipment_data_repository.delete_one(pk=data_id)
        await self.equipment_data_repository.save_changes()
