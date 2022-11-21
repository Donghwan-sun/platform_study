import datetime

from pydantic import BaseModel, EmailStr

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
    at_created: datetime.datetime

    class Config():
        orm_mode = True