from typing import List

from fastapi import APIRouter
from fastapi import status

from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.authentication.jwt_authentication import UserSession
from src.infrastructure.webserver.schemas.equpment_schemas import \
    EquipmentAlertDetail, EquipmentAlertCreate, EquipmentAlertUpdate
from src.controllers.equipment_alert_controller import \
    EquipmentAlertControllerDep

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[EquipmentAlertDetail]
)
async def get_equipment_alerts(
    alert_controller: EquipmentAlertControllerDep,
    user: UserSession, # noqa
):
    return await alert_controller.fetch_alerts()


@router.get(
    "/{alert_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentAlertDetail
)
async def get_equipment_alert(
    alert_controller: EquipmentAlertControllerDep,
    alert_id: IntPath,
    user: UserSession # noqa
):
    return await alert_controller.fetch_alert(alert_id=alert_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=EquipmentAlertDetail
)
async def create_equipment_alert(
    alert_controller: EquipmentAlertControllerDep,
    user: UserSession, # noqa
    request_data: EquipmentAlertCreate
):
    return await alert_controller.create_alert(
        request_data=request_data.dict()
    )


@router.put(
    "/{alert_id}",
    status_code=status.HTTP_200_OK,
    response_model=EquipmentAlertDetail
)
async def update_equipment_alert(
    alert_controller: EquipmentAlertControllerDep,
    user: UserSession, # noqa
    alert_id: IntPath,
    request_data: EquipmentAlertUpdate
):
    return await alert_controller.update_alert(
        alert_id=alert_id,
        request_data=request_data.dict()
    )


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_equipment_alert(
    alert_controller: EquipmentAlertControllerDep,
    user: UserSession, # noqa
    alert_id: IntPath,
):
    return await alert_controller.delete_alert(
        alert_id=alert_id
    )
