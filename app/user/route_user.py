from fastapi import APIRouter
from app.user.service_user import UserService
from app.user.repository_user import UserRepository
from app.user.schema_user import UserLogin

user_repo = UserRepository()
user_service = UserService(repository=user_repo)

router = APIRouter(prefix="/apiv1/users", tags=["users"])


@router.get("/")
async def read_users():
    return user_service.get()


@router.post("/")
async def create_user(user: UserLogin):
    return user_service.add(user)
