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
from src.infrastructure.database.sqlalchemy.config import get_db_session
from src.infrastructure.database.sqlalchemy.repositories.equipment_repository import \
    EquipmentRepository


class EquipmentController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.equipment_repository = EquipmentRepository(
            db_connection=db_connection
        )

    async def fetch_equipments(self):
        fetch_equipments_use_case = FetchEquipmentsUseCase(
            equipment_repository=self.equipment_repository
        )
        return await fetch_equipments_use_case.execute()

    async def fetch_equipment(self, *, equipment_id: int):
        fetch_equipment_use_case = FetchEquipmentUseCase(
            equipment_repository=self.equipment_repository
        )
        return await fetch_equipment_use_case.execute(equipment_id=equipment_id)

    async def create_equipment(self, *, request_data: dict):
        create_equipment_use_case = CreateEquipmentUseCase(
            equipment_repository=self.equipment_repository
        )
        return await create_equipment_use_case.execute(request_data=request_data)

    async def update_equipment(self, *, equipment_id: int, request_data: dict):
        update_equipment_use_case = UpdateEquipmentUseCase(
            equipment_repository=self.equipment_repository
        )
        return await update_equipment_use_case.execute(
            equipment_id=equipment_id,
            request_data=request_data
        )

    async def delete_equipment(self, *, equipment_id: int):
        delete_equipment_use_case = DeleteEquipmentUseCase(
            equipment_repository=self.equipment_repository
        )
        return await delete_equipment_use_case.execute(equipment_id=equipment_id)


EquipmentControllerDep: TypeAlias = Annotated[EquipmentController, Depends(EquipmentController)]
