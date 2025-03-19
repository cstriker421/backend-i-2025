import os
from sqlalchemy import Engine
from sqlmodel import Session
from session_13.models import Task



def get_engine()->Engine:
    DB_USER = os.getenv("DB_USER", None)
    DB_PASS = os.getenv("DB_PASS", None)
    DB_HOST = os.getenv("DB_HOST", None)
    DB_PORT = os.getenv("DB_PORT", None)
    DB_NAME = os.getenv("DB_NAME", None)
    engine = create_engine(f"postgresql://{DB_USER}")

get_session

def create_task(task: Task):
    assert task
    with get_session() as session:
        session.add(task)
        session.commit()