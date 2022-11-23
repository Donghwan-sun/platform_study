from fastapi import APIRouter
from account.views import user
from account.views import auth
api_router = APIRouter()
api_router.include_router(user.router, prefix="", tags=["users"])
api_router.include_router(auth.router, prefix="", tags=["auth"])

