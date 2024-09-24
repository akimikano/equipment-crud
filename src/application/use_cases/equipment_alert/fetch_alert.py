from src.application.repositories.equipment_alert_repository import \
    IEquipmentAlertRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class FetchEquipmentAlertUseCase(BaseUseCase):
    def __init__(self, *, equipment_alert_repository: IEquipmentAlertRepository):
        self.equipment_alert_repository = equipment_alert_repository

    async def execute(self, alert_id: int):
        return await self.equipment_alert_repository.fetch_one(pk=alert_id)
