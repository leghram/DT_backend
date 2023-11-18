from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.user.route_user import router as user_router
from app.user.service_user import UserService
from app.user.repository_user import UserRepository

from app.utils.handler_token import create_access_token

user_repo = UserRepository()
user_service = UserService(user_repo)

app = FastAPI()

app.include_router(user_router)


@app.get("/apiv1")
async def root():
    return {"msg": "Api Service"}


@app.post("/apiv1/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = user_service.get_by_username(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"user": user, "access_token": access_token, "token_type": "bearer"}
