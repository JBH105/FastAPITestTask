from pydantic import BaseModel
from typing import Optional

class TokenData(BaseModel):
    username: Optional[str] = None

class SignupUser(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PostCreate(BaseModel):
    content: str

class PostDisplay(BaseModel):
    id: int
    content: str
    owner_id: int

class UserLogin(BaseModel):
    email: str
    password: str
