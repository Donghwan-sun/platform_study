import datetime
from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool
    is_superuser: bool

class UserCreateResponse(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    at_created: date

    class Config():
        orm_mode = True