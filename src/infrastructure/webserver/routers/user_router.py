from typing import List

from starlette import status
from fastapi import APIRouter

from src.controllers.user import UserControllerDep
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.webserver.schemas.user_schemas import UserCreate, \
    UserDetail, UserUpdate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserDetail
)
async def create_user(
    user_controller: UserControllerDep,
    request_data: UserCreate
):
    return await user_controller.create_user(request_data=request_data.dict())


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[UserDetail]
)
async def get_users(
    user_controller: UserControllerDep,
):
    return await user_controller.fetch_users()


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserDetail
)
async def get_user(
    user_controller: UserControllerDep,
    user_id: IntPath
):
    return await user_controller.fetch_user(user_id=user_id)


@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserDetail
)
async def update_user(
    user_controller: UserControllerDep,
    request_data: UserUpdate,
    user_id: IntPath
):
    return await user_controller.update_user(
        user_id=user_id,
        data=request_data.dict()
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
async def delete_user(
    user_controller: UserControllerDep,
    user_id: IntPath
):
    return await user_controller.delete_user(user_id=user_id)

