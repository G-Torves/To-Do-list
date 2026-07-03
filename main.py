from fastapi import FastAPI

# Rodar com: uvicorn main:app --reload
app = FastAPI()
from task_routes import task_router
from user_routes import user_router

app.include_router(task_router)
app.include_router(user_router)