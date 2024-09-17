from typing import TypeVar, Sequence
from src.application.repositories.abstract_repository import AbstractRepository

Entity = TypeVar("Entity")
DbModel = TypeVar("DbModel")
DbConnection = TypeVar("DbConnection")


class BaseAsyncRepository(AbstractRepository):
    model: DbModel

    def __init__(self, db_connection: DbConnection):
        self.db_connection = db_connection

    async def save_one(self, *, entity: Entity):
        pass

    async def save_many(self, *, entity_list: Sequence[Entity]):
        pass

    async def delete_one(self, *, pk: int):
        pass

    async def delete_many(self, *, pk_list: Sequence[int]):
        pass

    async def fetch_many(self, **filters):
        pass

    async def fetch_one(self, *, pk: int, **filters):
        pass

    async def update_one(self, *, pk: int, data: dict):
        pass

    async def update_many(self, *, filters: dict, data: dict):
        pass

    async def save_changes(self):
        await self.db_connection.commit()
