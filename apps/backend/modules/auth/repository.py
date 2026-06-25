'''contains database logic for auth module'''
'''these are database operations, not business operations.'''
from sqlalchemy.orm import Session
from modules.auth.models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user