import uvicorn
from fastapi import FastAPI
from routes.LoginRoute import router as LoginRouter
from routes.ReadDataRoute import router as ReadDataRoute

app = FastAPI(description="Empresa EldenLabs", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Bienvenidos a EldenLabs"}


app.include_router(
    LoginRouter,
    tags=["login"],
    prefix="/api/v1/login"
)

app.include_router(
    ReadDataRoute,
    tags=["read-data"],
    prefix="/api/v1/read-data"
)

if __name__ == "__main__":
    uvicorn.run("main:app")
