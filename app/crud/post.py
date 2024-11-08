from sqlalchemy.orm import Session
from ..models import Post

class PostCRUD:
    def get(self, db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()

    def create(self, db: Session, title: str, content: str, user_id: int):
        post = Post(title=title, content=content, user_id=user_id)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    def update(self, db: Session, post_id: int, title: str = None, content: str = None):
        post = self.get(db, post_id)
        if post:
            if title:
                post.title = title
            if content:
                post.content = content
            db.commit()
            db.refresh(post)
        return post

    def delete(self, db: Session, post_id: int):
        post = self.get(db, post_id)
        if post:
            db.delete(post)
            db.commit()
        return post
