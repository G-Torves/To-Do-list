from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=['Usuarios'])

@auth_router.get('/')
async def auth():
    """
    Rota padrão de autenticação.
    """
    return {'Mensagem': 'O usuario esta autenticado?', 'autenticado': False}

@auth_router.get('/add')
async def add():
    """
    Rota responsavel por adicionar usuarios.
    """
    return {'Mensagem': 'Usuario adicionado com sucesso.'}

@auth_router.get('/delete')
async def delete():
    """
    Rota responsavel por deletar usuarios.
    """
    return {'Mensagem': 'Usuario deletado com sucesso.'}

@auth_router.get('/info')
async def info():
    """
    Rota reponsavel por mostrar informacoes do usuario.
    """
    return {'Mensagem': 'Tarefas concluidas ... Tarefas em andamento ... Tarefas totais'}