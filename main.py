from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

# Rodar com: uvicorn main:app --reload
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

from task_routes import task_router
from auth_routes import auth_router

app.include_router(task_router)
app.include_router(auth_router)