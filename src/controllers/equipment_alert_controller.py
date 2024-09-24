from typing import TypeAlias, Annotated

from fastapi import Depends

from src.application.use_cases.equipment.create_equipment import \
    CreateEquipmentUseCase
from src.application.use_cases.equipment.delete_equipment import \
    DeleteEquipmentUseCase
from src.application.use_cases.equipment.fetch_equipment import \
    FetchEquipmentUseCase
from src.application.use_cases.equipment.fetch_equipments import \
    FetchEquipmentsUseCase
from src.application.use_cases.equipment.update_equipment import \
    UpdateEquipmentUseCase
from src.application.use_cases.equipment_alert.create_alert import \
    CreateEquipmentAlertUseCase
from src.application.use_cases.equipment_alert.delete_alert import \
    DeleteEquipmentAlertUseCase
from src.application.use_cases.equipment_alert.fetch_alert import \
    FetchEquipmentAlertUseCase
from src.application.use_cases.equipment_alert.fetch_alerts import \
    FetchEquipmentAlertsUseCase
from src.application.use_cases.equipment_alert.update_alert import \
    UpdateEquipmentAlertUseCase
from src.infrastructure.database.sqlalchemy.config import get_db_session
from src.infrastructure.database.sqlalchemy.repositories.equipment_alert_repository import \
    EquipmentAlertRepository
from src.infrastructure.database.sqlalchemy.repositories.equipment_repository import \
    EquipmentRepository


class EquipmentAlertController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.equipment_alert_repository = EquipmentAlertRepository(
            db_connection=db_connection
        )

    async def fetch_alerts(self):
        fetch_alerts_use_case = FetchEquipmentAlertsUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await fetch_alerts_use_case.execute()

    async def fetch_alert(self, *, alert_id: int):
        fetch_alert_use_case = FetchEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await fetch_alert_use_case.execute(alert_id=alert_id)

    async def create_alert(self, *, request_data: dict):
        create_alert_use_case = CreateEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await create_alert_use_case.execute(request_data=request_data)

    async def update_alert(self, *, alert_id: int, request_data: dict):
        update_alert_use_case = UpdateEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await update_alert_use_case.execute(
            alert_id=alert_id,
            request_data=request_data
        )

    async def delete_alert(self, *, alert_id: int):
        delete_alert_use_case = DeleteEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await delete_alert_use_case.execute(alert_id=alert_id)


EquipmentAlertControllerDep: TypeAlias = Annotated[
    EquipmentAlertController,
    Depends(EquipmentAlertController)
]
