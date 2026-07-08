from fastapi import APIRouter

task_router = APIRouter(prefix="/task", tags=['Tarefas'])

@task_router.get('/')
async def lista():
    """
    Rota responsavel por buscar as tarefas existentes.
    """
    return {"Mensagem": "As tarefas existentes são: ..."}

@task_router.get('/add')
async def add():
    """
    Rota responsavel por adicionar tarefas.
    """
    return {'Mensagem': 'Tarefa adicionada com sucesso.'}

@task_router.get('/delete')
async def delete():
    """
    Rota reponsavel por deletar tarefas.
    """
    return {'Mensagem': 'Tarefa excluida com sucesso.'}

@task_router.get('/conclude')
async def conclude():
    """
    Rota responsavel por concluir tarefas.
    """
    return {'Mensagem': 'Tarefa concluida com sucesso.'}