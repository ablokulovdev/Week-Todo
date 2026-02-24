from datetime import datetime
from pydantic import BaseModel



class TaskListRespons(BaseModel):
    
    id: int
    title: str
    description: str | None = None
    status: str
    due_date: datetime | None = None
    user_id:int
    
    created_at: datetime
    updated_at: datetime
    
    class Config():
        from_attributes = True