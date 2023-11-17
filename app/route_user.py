from fastapi import APIRouter

router = APIRouter(prefix="/apiv1/users", tags=["users"])


@router.get("/")
async def read_users():
    print("que pasa")
    return [{"name": "Miguel", "email": "miguel@gmail.com"}]
