'''contains buiness logic for auth module'''
from modules.auth.repository import UserRepository
from sqlalchemy.orm import Session
from utils import pwd_hasher
from modules.auth.models import User
from modules.auth.schemas import UserCreate

class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(self, 
                      data: UserCreate):
        # Here you can add any business logic related to user registration
        # For example, you can hash the password before saving it to the database

        # raise exception if user is already thier
        hashed_password = pwd_hasher.hash(data.password)
        user = User(username=data.username, 
                    email=data.email, 
                    hashed_password=hashed_password)
        return self.user_repository.create(user)