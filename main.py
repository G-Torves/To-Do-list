from fastapi import FastAPI

# Rodar com: uvicorn main:app --reload
app = FastAPI()
from task_routes import task_router
from auth_routes import auth_router

app.include_router(task_router)
app.include_router(auth_router)