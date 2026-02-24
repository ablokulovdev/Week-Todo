from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Form,
    Depends,
    HTTPException
)

from app.dependencies import get_db
from app.models.user import User
from app.services.aut import hashed_pass, passwor_verify
from app.schemas.user import UserListRespons


router = APIRouter(
    prefix="/users",
    tags=["User Endpoint."]
)


@router.post("/register",response_model=UserListRespons)
def register(
    username: str = Form(min_length=3,max_length=20),
    password: str = Form(min_length=8),
    full_name: str = Form(),
    phone: str = Form(),
    db: Session = Depends(get_db)
):
    
    exists = db.query(User).filter(User.username == username).first()
    if exists:
        raise HTTPException(status_code=400,detail="user already exists")
    
    hashed = hashed_pass(password)
    
    new_user = User(
        username=username,
        hashed_password=hashed,
        full_name=full_name,
        phone=phone
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    
    
@router.get("/login",response_model=UserListRespons)
def login(
    username: str = Form(),
    password: str = Form(),
    db: Session = Depends(get_db)
):
    
    users = db.query(User).filter(User.username == username).first()
    
    if users:
        
        if passwor_verify(password,users.hashed_password):
            
            return users
        
        else:
            raise HTTPException(status_code=400,detail="password not correct")
    
    else:
        raise HTTPException(status_code=400,detail="User not exists")
    
    