from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings_utils import get_settings

SQLALCHEMY_DATABASE_URL = f"{get_settings().ENGINE}://{get_settings().USER}@{get_settings().PASSWORD}@{get_settings().HOST}:{get_settings().PORT}/{get_settings().DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
