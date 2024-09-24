from src.application.exceptions import NotFound
from src.application.repositories.equipment_data_repository import \
    IEquipmentDataRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class UpdateEquipmentDataUseCase(BaseUseCase):
    def __init__(self, *, equipment_data_repository: IEquipmentDataRepository):
        self.equipment_data_repository = equipment_data_repository

    async def execute(self, data_id: int, request_data: dict):
        db_data = await self.equipment_data_repository.fetch_one(pk=data_id)
        if not db_data:
            raise NotFound

        db_data = await self.equipment_data_repository.update_one(
            pk=data_id,
            data=request_data
        )
        await self.equipment_data_repository.save_changes()
        return db_data
