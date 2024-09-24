from fastapi import APIRouter
from fastapi import status

from src.controllers.equipment_data_controller import EquipmentDataControllerDep
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.authentication.jwt_authentication import UserSession
from src.infrastructure.webserver.schemas.equpment_schemas import \
    EquipmentDataDetail, EquipmentDataCreate, EquipmentDataUpdate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=EquipmentDataDetail
)
async def create_equipment_data(
    data_controller: EquipmentDataControllerDep,
    user: UserSession, # noqa
    request_data: EquipmentDataCreate
):
    return await data_controller.create_data(
        request_data=request_data.dict()
    )


@router.put(
    "/{data_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentDataDetail
)
async def update_equipment_data(
    data_controller: EquipmentDataControllerDep,
    user: UserSession, # noqa
    data_id: IntPath,
    request_data: EquipmentDataUpdate
):
    return await data_controller.update_data(
        data_id=data_id,
        request_data=request_data.dict()
    )


@router.delete(
    "/{data_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_equipment_data(
    data_controller: EquipmentDataControllerDep,
    user: UserSession, # noqa
    data_id: IntPath,
):
    return await data_controller.delete_data(
        data_id=data_id
    )
