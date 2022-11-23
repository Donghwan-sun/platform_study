from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi_jwt_auth import exceptions
from sqlalchemy.orm import Session

from schema.account.auth import UserLoginResponse, UserLogin
from utils.database.session import get_db
from account.services.auth import user_certification, create_access_tokens, create_init_refresh_tokens, refresh_token
from common.oauth2 import AuthJWT

router = APIRouter(prefix="/v1/auth")

@router.post("/login", response_model=UserLoginResponse)
def login(user: UserLogin, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    user_cerifi = user_certification(email=user.email, password=user.password, db= db)
    access_token = create_access_tokens(Authorize, email=user.email)
    refresh_tokens = create_init_refresh_tokens(Authorize, email=user.email)

    return {"access_token" : access_token, "refresh_token": refresh_tokens}

@router.delete("/logout")
def logout(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        Authorize.unset_jwt_cookies()
        return {"msg": "Successfully logout"}

    except Exception as e:
        if isinstance(e, exceptions.MissingTokenError):
            return e
        return e


@router.post("/refresh")
def token_refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = refresh_token(current_user)
    return {"access_token": new_access_token}

@router.get("/auth_user_test")
def user_only_test(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        cur_user = Authorize.get_jwt_subject()
        return cur_user

    except Exception as e:
        if isinstance(e, exceptions.MissingTokenError):
            return e