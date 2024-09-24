from src.application.exceptions import NotFound
from src.application.repositories.equipment_alert_repository import \
    IEquipmentAlertRepository
from src.application.use_cases.user.base_use_case import BaseUseCase


class UpdateEquipmentAlertUseCase(BaseUseCase):
    def __init__(self, *, equipment_alert_repository: IEquipmentAlertRepository):
        self.equipment_alert_repository = equipment_alert_repository

    async def execute(self, alert_id: int, request_data: dict):
        db_alert = await self.equipment_alert_repository.fetch_one(pk=alert_id)
        if not db_alert:
            raise NotFound

        db_alert = await self.equipment_alert_repository.update_one(
            pk=alert_id,
            data=request_data
        )
        await self.equipment_alert_repository.save_changes()
        return db_alert
