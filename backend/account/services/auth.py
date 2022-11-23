from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from account.models.user import Users
from common.hash import Hasher
def create_access_tokens(Authorize, email):
    access_token = Authorize.create_access_token(subject=email)
    Authorize.set_access_cookies(access_token)

    return access_token

def create_init_refresh_tokens(Authorize, email):
    refresh_token = Authorize.create_refresh_token(subject=email)
    Authorize.set_refresh_cookies(refresh_token)

    return refresh_token

def refresh_token(Authorize, user):
    new_access_token = Authorize.create_access_token(subject=user)
    Authorize.set_refresh_cookies(new_access_token)

    return new_access_token

def user_certification(email, password, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Email or Password")

    certification_result = Hasher.password_verify(password, hassed_password=user.password)
    if not certification_result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Email or Password")
    return certification_result