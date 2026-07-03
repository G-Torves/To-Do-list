from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=['Usuarios'])

@user_router.get('/')
async def users():
    """
    Rota responsavel por mostrar todos usuarios atuais.
    """
    return {'Mensagem': 'Os usuarios atuais são: ...'}