from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.config import settings
from utils.database.base import Base
from utils.database.session import engine
from account.urls import api_router


def include_router(app):
    app.include_router(api_router)

def include_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_LIST,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOW_METHOD,
        allow_headers=settings.ALLOW_HEADERS
    )
def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    include_middleware(app)
    create_tables()
    return app
