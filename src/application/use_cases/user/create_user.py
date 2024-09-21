from src.application.repositories.user_repository import IUserRepository
from src.application.use_cases.user.base_use_case import BaseUseCase
from src.domain.entities.user import UserEntity
from src.domain.services.auth import get_password_hash


class CreateUserUseCase(BaseUseCase):
    def __init__(self, *, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, request_data: dict):
        raw_password = request_data.pop("password")

        user = UserEntity(
            id=None,
            password_hash=get_password_hash(password=raw_password),
            **request_data
        )

        await self.user_repository.save_one(entity=user)
        await self.user_repository.save_changes()
        return user
