from db.base import Base
from db.session import engine

from modules.auth.models import User

Base.metadata.create_all(bind=engine)

print("Tables Created")