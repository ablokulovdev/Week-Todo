from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.dependencies import get_db
from app.models.task import Task
from app.schemas.task import TaskListRespons
from typing import List


router = APIRouter(
    prefix="/tasks",
    tags=["Task Endpoint"]
)


@router.get("", response_model=List[TaskListRespons])
def get_task(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks