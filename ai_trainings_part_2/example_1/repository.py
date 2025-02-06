from models import User
from db import db

class UserRepository:
    def add_user(self, user_dto):
        user = User(username=user_dto.username, email=user_dto.email)
        db.session.add(user)
        db.session.commit()
        return user
