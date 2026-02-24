from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    username = Column(String(length=50),unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    full_name = Column(String)
    phone = Column(String(length=20))
    
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"User (id = {self.id}, username = {self.username}, phone = {self.phone})"