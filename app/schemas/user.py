from datetime import datetime
from pydantic import BaseModel


class UserListRespons(BaseModel):
    
    id: int
    username: str
    full_name: str 
    phone: str
    created_at: datetime
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True