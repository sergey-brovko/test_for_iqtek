from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from contextlib import asynccontextmanager
from src.config import settings
from src.dependencies import get_repository
from src.repositories.base import Repository
from src.schemas import UserRepository, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.repository_type == "sql":
        from src.database import create_tables
        await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/user/{user_id}", response_model=UserRepository)
async def get_user(user_id: int, rep: Repository = Depends(get_repository)):
    response = await rep.get_user(user_id)
    if not response:
        raise HTTPException(status_code=404, detail="User not found")
    return response

@app.post("/user", response_model=UserRepository)
async def create_user(user: User, rep: Repository = Depends(get_repository)):
    return await rep.create_user(user)

@app.delete("/user/{user_id}")
async def delete_user(user_id: int, rep: Repository = Depends(get_repository)):
    success = await rep.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return f"User {user_id} deleted"

@app.patch("/user")
async def update_user(user_id: int, user: User, rep: Repository = Depends(get_repository)):
    success = await rep.update_user(user_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return f"User {user_id} updated"