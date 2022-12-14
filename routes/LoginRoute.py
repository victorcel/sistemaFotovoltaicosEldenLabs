import os
import uuid

from fastapi import Depends, APIRouter, HTTPException

from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from models.UserModel import UserCreateModel, UserModel

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
async def register(user: UserCreateModel):
    """
    Endpoint Register Users

    Este endpoint es usado para la creacion de usuarios que estarian
    utilizando esta aplicacion.

    """
    if user.email in DB["users"]:
        raise HTTPException(status_code=400, detail="this email already exists")

    db_user = UserModel(**user.dict(), id=uuid.uuid4())
    DB["users"][db_user.email] = db_user
    print(DB)
    return {"detail": "Successful Registered"}


@router.post(TOKEN_URL)
async def login(data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint Login User

    En este endpoint se realiza la autenticacion del usuario, en caso que las
    credenciales no sean las correctas genera el error.

    """
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


@router.get("/test-token")
async def test_token(user=Depends(manager)):
    """
    Endpoint Test Token

    Este Endpoint es utilizado para realizar pruebas si el token es correcto
    y puede servir mas adelante para refrescar el token.
    """
    return {"detail": f"Welcome {user.email}"}
