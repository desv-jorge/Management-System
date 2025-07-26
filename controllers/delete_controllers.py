from models.user import Model_user_one

from services.user_delete import delete_user

from fastapi import HTTPException, status


async def user_delete(email: Model_user_one):

    delete_response = await delete_user(email)
    print(f"\n {delete_response}")

    if(delete_response == True):
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Usuário deletado com sucesso")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")