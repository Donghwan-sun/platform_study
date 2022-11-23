from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schema.account.user import UserCreate, UserCreateResponse
from utils.database.session import get_db
from account.services.user import create_user, verify_user

router = APIRouter(prefix="/v1/users")
@router.post("/register", response_model=UserCreateResponse)
def register(user: UserCreate,  db: Session = Depends(get_db)):
    username, email = verify_user(user.email, user.username, db)

    if username or email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Account already exist")

    user = create_user(user, db)
    return user
