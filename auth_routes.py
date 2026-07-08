from fastapi import APIRouter , Depends
from dependencies import catch_session
from models import Usuario

auth_router = APIRouter(prefix="/auth", tags=['Usuarios'])

@auth_router.get('/')
async def auth():
    """
    Rota padrão de autenticação.
    """
    return {'Mensagem': 'O usuario esta autenticado?', 'autenticado': False}

@auth_router.post('/add')
async def add(nome: str, email: str, senha: str, session = Depends(catch_session)):
    """
    Rota responsavel por adicionar usuarios.
    """
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {'Mensagem': 'Usuario ja existente com este email!'}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
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