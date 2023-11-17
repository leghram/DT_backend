from fastapi import FastAPI
from app.user.route_user import router as user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/apiv1")
async def root():
    return {"msg": "Api Service"}
