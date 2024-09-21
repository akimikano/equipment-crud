from typing import List

from fastapi import APIRouter
from fastapi import status

from src.controllers.equipment_controller import EquipmentControllerDep
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.webserver.schemas.equpment_schemas import \
    EquipmentDetail, EquipmentCreate

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[EquipmentDetail]
)
async def get_equipments(
    equipment_controller: EquipmentControllerDep,
    # admin: AdminSession, # noqa
):
    return await equipment_controller.fetch_equipments()


@router.get(
    "/{equipment_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentDetail
)
async def get_equipment(
    equipment_controller: EquipmentControllerDep,
    equipment_id: IntPath
    # admin: AdminSession, # noqa
):
    return await equipment_controller.fetch_equipment(equipment_id=equipment_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=EquipmentDetail
)
async def create_equipment(
    equipment_controller: EquipmentControllerDep,
    # admin: AdminSession, # noqa
    request_data: EquipmentCreate
):
    return await equipment_controller.create_equipment(
        request_data=request_data.dict()
    )


@router.put(
    "/{equipment_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentDetail
)
async def update_equipment(
    equipment_controller: EquipmentControllerDep,
    # admin: AdminSession, # noqa
    equipment_id: IntPath,
    request_data: EquipmentCreate
):
    return await equipment_controller.update_equipment(
        equipment_id=equipment_id,
        request_data=request_data.dict()
    )


@router.delete(
    "/{equipment_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_equipment(
    equipment_controller: EquipmentControllerDep,
    # admin: AdminSession, # noqa
    equipment_id: IntPath,
):
    return await equipment_controller.delete_equipment(
        equipment_id=equipment_id,
    )
