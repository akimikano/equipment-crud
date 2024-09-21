from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.equipment import EquipmentEntity
from src.application.repositories.equipment_repository import \
    IEquipmentRepository


class FetchEquipmentsUseCase(BaseUseCase):
    def __init__(self, *, equipment_repository: IEquipmentRepository):
        self.equipment_repository = equipment_repository

    async def execute(self):
        return await self.equipment_repository.fetch_many()
