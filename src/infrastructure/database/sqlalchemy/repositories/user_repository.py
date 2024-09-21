from src.application.repositories.user_repository import IUserRepository
from src.domain.entities.user import UserEntity
from src.infrastructure.database.sqlalchemy.models import UserModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository, DbModel


class UserRepository(BaseAsyncRepository, IUserRepository):
    model = UserModel

    @staticmethod
    def to_entity(db_instance: UserModel):
        return UserEntity(
            id=db_instance.id,
            first_name=db_instance.first_name,
            last_name=db_instance.last_name,
            email=db_instance.email,
            auth_type=db_instance.auth_type,
            password_hash=db_instance.password_hash
        )

