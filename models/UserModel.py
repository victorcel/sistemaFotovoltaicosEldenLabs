from pydantic import BaseModel, EmailStr, UUID4, Field


class UserCreatemodel(BaseModel):
    email: EmailStr = Field(default=..., example="vbarrera@outlook.com")
    password: str = Field(default=..., example="123456")


class UserModel(UserCreatemodel):
    id: UUID4
