from typing import TypeAlias, Annotated

from fastapi import Depends

from src.infrastructure.database.sqlalchemy.config import get_db_session
from src.infrastructure.database.sqlalchemy.repositories.equipment_alert_repository import \
    EquipmentAlertRepository
from src.infrastructure.database.sqlalchemy.repositories.equipment_data_repository import \
    EquipmentDataRepository


class EquipmentDataController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.equipment_data_repository = EquipmentDataRepository(
            db_connection=db_connection
        )

    async def fetch_many_data(self):
        fetch_many_data_use_case = FetchEquipmentAlertsUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await fetch_many_data_use_case.execute()

    async def fetch_one_data(self, *, data_id: int):
        fetch_one_data_use_case = FetchEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await fetch_alert_use_case.execute(alert_id=alert_id)

    async def create_data(self, *, request_data: dict):
        create_data_use_case = CreateEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await create_data_use_case.execute(request_data=request_data)

    async def update_data(self, *, data_id: int, request_data: dict):
        update_data_use_case = UpdateEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await update_data_use_case.execute(
            alert_id=alert_id,
            request_data=request_data
        )

    async def delete_data(self, *, data_id: int):
        delete_data_use_case = DeleteEquipmentAlertUseCase(
            equipment_alert_repository=self.equipment_alert_repository
        )
        return await delete_data_use_case.execute(alert_id=alert_id)


EquipmentDataControllerDep: TypeAlias = Annotated[
    EquipmentDataController,
    Depends(EquipmentDataController)
]
