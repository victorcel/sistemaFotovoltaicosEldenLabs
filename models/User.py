from pydantic import BaseModel, EmailStr, UUID4


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(UserCreate):
    id: UUID4


