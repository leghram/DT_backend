from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.conection.db_client_provider import SesionProvider
from app.user.service_user import UserService
from app.user.repository_user import UserRepository

user_repo = UserRepository()
user_service = UserService(repository=user_repo)

router = APIRouter(prefix="/apiv1/users", tags=["users"])


@router.get("/")
async def read_users(session: Session = Depends(SesionProvider)):
    return user_service.get()
