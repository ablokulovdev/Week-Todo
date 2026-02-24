import enum
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Enum,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class TaskStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
    cancelled = "cancelled"


class Task(Base):
    
    __tablename__ = "tasks"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    description = Column(Text)
    status = Column(Enum(TaskStatus),default=TaskStatus.pending)
    due_date = Column(DateTime)
    user_id = Column(ForeignKey("users.id"),nullable=False) 
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User",back_populates="tasks")
    
    
    
    def __repr__(self):
        return f"Task (id = {self.id}, title = {self.title}, status = {self.status}) "