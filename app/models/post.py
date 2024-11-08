from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    board_id = Column(Integer)
    title = Column(String)
    content = Column(String)
    view_count = Column(Integer)
    del_yn = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")
