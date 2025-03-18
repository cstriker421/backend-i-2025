from fastapi import FastAPI
from session_12.models import Task

api = FastAPI(
    title = "ETIC_Algarve Class API"
)

@api.get("/task",response_model=Task)
def get_task():
    pass

@api.post("/task")
def create_task():
    pass

@api.put("/task")
def edit_task():
    pass

@api.patch("/task")
def close_task():
    pass

@api.delete("/task")
def delete_task():
    pass