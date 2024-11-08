from sqlalchemy.orm import Session
from ..models import User

class UserCRUD:
    def get(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def create(self, db: Session, username: str, email: str):
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, user_id: int, username: str = None, email: str = None):
        user = self.get(db, user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            db.commit()
            db.refresh(user)
        return user

    def delete(self, db: Session, user_id: int):
        user = self.get(db, user_id)
        if user:
            db.delete(user)
            db.commit()
        return user
