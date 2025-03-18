import os
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    title: str
    description: str
    due_date: datetime
    is_done: bool = False

DB_USER = os.getenv("DB_USER", None)
DB_PASS = os.getenv("DB_PASS", None)
DB_HOST = os.getenv("DB_HOST", None)
DB_PORT = os.getenv("DB_PORT", None)
DB_NAME = os.getenv("DB_NAME", None)

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

SQLModel.metadata.create_all(engine)