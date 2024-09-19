from pydantic import BaseModel, EmailStr

from src.domain.enums import AuthType


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    auth_type: AuthType


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserDetail(UserBase):
    id: int
