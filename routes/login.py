import os
import uuid

from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from models.User import UserCreate, User

DEFAULT_SETTINGS = os.getenv("SECRET_FAST_API")

router = APIRouter()

TOKEN_URL = "/auth/token"

manager = LoginManager(DEFAULT_SETTINGS, TOKEN_URL)

DB = {
    "users": {}
}


@manager.user_loader
def get_user(email: str):
    return DB["users"].get(email)


@router.post("/register")
async def register(user: UserCreate):
    """
    Register Users

    Este endpoint es usado para la creacion de usuarios que estarian
    utilizando esta aplicacion

    """
    if user.email in DB["users"]:
        raise HTTPException(status_code=400, detail="this email already exists")

    db_user = User(**user.dict(), id=uuid.uuid4())
    DB["users"][db_user.email] = db_user
    return {"detail": "Successful Registered"}


@router.post(TOKEN_URL)
async def login(data: OAuth2PasswordRequestForm):
    email = data.username
    password = data.password

    user = get_user(email)

    if not user:
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=email)
    )

    return {"access_token": access_token, "token_type": "bearer"}
