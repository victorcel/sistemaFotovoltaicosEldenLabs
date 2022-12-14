import uuid

from fastapi import FastAPI, HTTPException

from models.User import UserCreate, User

app = FastAPI()

DB = {
    "users": {}
}


@app.post("/register")
async def register(user: UserCreate):
    if user.email in DB["users"]:
        raise HTTPException(status_code=400, detail="this email already exists")

    db_user = User(**user.dict(), id=uuid.uuid4())
    DB["users"][db_user.email] = db_user
    return {"detail": "Successful Registered"}


