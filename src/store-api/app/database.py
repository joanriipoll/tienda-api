import os
from sqlmodel import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Variable DATABASE_URL is not configured")

DB_ECHO = os.getenv("DB_ECHO", "False").lower() in ("true", "1", "t", "yes")

engine = create_engine(DATABASE_URL, echo=DB_ECHO)