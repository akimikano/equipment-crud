from abc import ABC

from src.application.repositories.abstract_repository import AbstractRepository


class IUserRepository(ABC, AbstractRepository):
    ...


