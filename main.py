from fastapi import FastAPI

app = FastAPI()
from task_routes import task_router

app.include_router(task_router)