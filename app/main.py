from fastapi import FastAPI

from app.routers.user import router as user_router
from app.routers.task import router as task_router

from app.db.database import initial_db


initial_db()

app = FastAPI(title="Week Todo")

app.include_router(user_router)
app.include_router(task_router)

