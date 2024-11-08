from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

from .database import SessionLocal, init_db
from . import models
from . import crud

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.user.get(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@app.post("/user/")
def create_new_user(username: str, email: str, db: Session = Depends(get_db)):
    return {"user": crud.user.create(db, username, email)}

@app.put("/user/{user_id}")
def update_existing_user(user_id: int, username: str = None, email: str = None, db: Session = Depends(get_db)):
    user = crud.user.update(db, user_id, username, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@app.delete("/user/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.user.delete(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

@app.get("/post/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.post.get(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post": post}

@app.post("/post/")
def create_new_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    return {"post": crud.post.create(db, title, content, user_id)}

@app.put("/post/{post_id}")
def update_existing_post(post_id: int, title: str = None, content: str = None, db: Session = Depends(get_db)):
    post = crud.post.update(db, post_id, title, content)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post": post}

@app.delete("/post/{post_id}")
def delete_existing_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.post.delete(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
