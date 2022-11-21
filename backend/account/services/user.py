from sqlalchemy.orm import Session

from common.hash import Hasher
from schema.account.user import UserCreate
from account.models.user import Users

def create_user(user: UserCreate, db: Session):
    user = Users(
        username=user.username,
        email=user.email,
        password=Hasher.get_hashed_password(user.password),
        is_active=user.is_acitve,
        is_superuser=user.is_superuser
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def verify_user(email, username, db: Session):
    username = db.query(Users).filter(Users.username == username).first()
    email = db.query(Users).filter(Users.email == email).first()

    return username, email