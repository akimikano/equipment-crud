from src.application.repositories.equipment_data_repository import \
    IEquipmentDataRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class FetchEquipmentManyDataUseCase(BaseUseCase):
    def __init__(self, *, equipment_data_repository: IEquipmentDataRepository):
        self.equipment_data_repository = equipment_data_repository

    async def execute(self):
        return await self.equipment_data_repository.fetch_many()
