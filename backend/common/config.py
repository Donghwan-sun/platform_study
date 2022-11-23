import os
from pytz import timezone
from dotenv import load_dotenv

env_path = ".env"
load_dotenv(dotenv_path=env_path)

class Settings():
    # PROJECT SETTINGS
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION")

    # DATABASE SETTINGS
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY = os.getenv("SECRET_KEY")
    # TIME SETTINGS
    TIMEZONE = timezone("Asia/Seoul")
    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

    # CORS ALLOW SETTINGS
    ALLOW_LIST = ["*"]
    ALLOW_METHOD = ["*"]
    ALLOW_HEADERS = ["*"]
    ALLOW_CREDENTIALS = True

settings = Settings()
