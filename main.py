import uvicorn
from fastapi import FastAPI
from routes.login import router as LoginRouter

app = FastAPI(description="Empresa EldenLabs", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Bienvenidos a EldenLabs"}


app.include_router(LoginRouter, tags=["login"], prefix="/api/v1/login")

if __name__ == "__main__":
    uvicorn.run("main:app")
