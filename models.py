from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

# Alembic
# 1. alembic init alembic                         { Inicia o alembic }
# 2. alembic revision --autogenerate -m "message" { Cria uma nova versão }
# 3. alembic upgrade head                         { Cria o banco de dados }

db = create_engine("sqlite:///banco.db")
Base = declarative_base()

# Usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Tarefas
class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario = Column("usuario", ForeignKey("usuarios.id"), nullable=False)
    titulo = Column("titulo", String, nullable=False)
    descricao = Column("descricao", String, nullable=False)
    status = Column("status", Boolean, default=True)

    def __init__(self, usuario, descricao, status=True):
        self.usuario = usuario
        self.descricao = descricao
        self.status = status