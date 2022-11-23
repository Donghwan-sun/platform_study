from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from common.config import settings

class Settings(BaseModel):
    authjwt_secret_key: str = settings.SECRET_KEY

    #xss 공격대비 설정
    authjwt_token_location: set = {"cookies"} # csrf 보호 포함
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_secure: bool = False

@AuthJWT.load_config
def get_config():
    return Settings()

