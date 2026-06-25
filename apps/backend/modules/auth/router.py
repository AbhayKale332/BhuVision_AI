'''A router's responsibility should be limited to:

Defining API endpoints (GET, POST, PUT, DELETE, ...)
Receiving request data
Calling the appropriate service
Returning the response
Declaring dependencies (authentication, database session, etc.)'''

from fastapi import APIRouter, Depends
from modules.auth.service import AuthService
from sqlalchemy.orm import Session
from core.dependencies import get_db
from modules.auth.schemas import UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
def register_user(data: UserCreate, 
                  db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    return auth_service.register_user(data)
    