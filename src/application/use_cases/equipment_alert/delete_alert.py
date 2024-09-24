from src.application.repositories.equipment_alert_repository import \
    IEquipmentAlertRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class DeleteEquipmentAlertUseCase(BaseUseCase):
    def __init__(self, *, equipment_alert_repository: IEquipmentAlertRepository):
        self.equipment_alert_repository = equipment_alert_repository

    async def execute(self, alert_id: int):
        await self.equipment_alert_repository.delete_one(pk=alert_id)
        await self.equipment_alert_repository.save_changes()
