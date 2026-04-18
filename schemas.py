from pydantic import BaseModel

# what is expected when someone signs up
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# what is sent back after creating user
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

# what is sent back after successful login
class Token(BaseModel):
    access_token: str
    token_type: str
    