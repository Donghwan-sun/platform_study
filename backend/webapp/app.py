from fastapi import FastAPI
from common.config import settings
from utils.database.base import Base
from utils.database.session import engine
from account.urls import api_router