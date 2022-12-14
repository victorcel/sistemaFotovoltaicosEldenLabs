from fastapi import FastAPI

app = FastAPI(description="Empresa EldenLabs", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Bienvenidos a EldenLabs"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
