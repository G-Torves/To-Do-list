from fastapi import APIRouter

task_router = APIRouter(prefix="/task", tags=['Tarefas'])

@task_router.get('/')
async def lista():
    """
    Rota responsavel por buscar as tarefas existentes.
    """
    return {"mensagem": "As tarefas existentes são: ..."}