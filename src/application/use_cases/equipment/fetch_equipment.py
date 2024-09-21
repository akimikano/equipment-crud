from src.application.use_cases.user.base_use_case import BaseUseCase
from src.application.repositories.equipment_repository import \
    IEquipmentRepository


class FetchEquipmentUseCase(BaseUseCase):
    def __init__(self, *, equipment_repository: IEquipmentRepository):
        self.equipment_repository = equipment_repository

    async def execute(self, *, equipment_id: int):
        return await self.equipment_repository.fetch_one(
            pk=equipment_id
        )
