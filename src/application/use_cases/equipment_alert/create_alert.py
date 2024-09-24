from src.application.repositories.equipment_alert_repository import \
    IEquipmentAlertRepository
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.equipment_alert import EquipmentAlertEntity


class CreateEquipmentAlertUseCase(BaseUseCase):
    def __init__(self, *, equipment_alert_repository: IEquipmentAlertRepository):
        self.equipment_alert_repository = equipment_alert_repository

    async def execute(self, request_data: dict):

        equipment_alert = EquipmentAlertEntity(
            id=None,
            **request_data
        )

        await self.equipment_alert_repository.save_one(entity=equipment_alert)
        await self.equipment_alert_repository.save_changes()
        return equipment_alert
