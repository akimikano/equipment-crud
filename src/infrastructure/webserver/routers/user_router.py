from typing import List

from fastapi import APIRouter
from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.user_controller import UserControllerDep
from src.infrastructure.database.sqlalchemy.config import get_db_session, \
    DbSession
from src.infrastructure.database.sqlalchemy.models import UserModel
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.webserver.settings import settings
from src.infrastructure.webserver.schemas.user_schemas import UserCreate, \
    UserDetail, UserUpdate, Token, UserLogin
from src.infrastructure.authentication.jwt_authentication import \
    JWTAuthenticationDep, UserSession

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


@router.post("/jwt-create", response_model=Token)
async def create_jwt(
    request_data: UserLogin,
    jwt_authentication: JWTAuthenticationDep
):
    return await jwt_authentication.authenticate(
        email=request_data.email,
        password=request_data.password
    )


@router.get("/profile/me", response_model=UserDetail)
async def read_users_me(
    current_user: UserSession,
):
    return current_user
