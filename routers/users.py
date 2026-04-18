from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserResponse, Token
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

# signup endpoint
@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # check if username exists
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")
    # hash password before saving
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    # save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# login endpoint
@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    # find user in database
    db_user = db.query(User).filter(User.username == user.username).first()
    # if user doesn't exist or password is wrong, return error
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # create & return a token
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}
