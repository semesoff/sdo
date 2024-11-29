from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest):
    # TODO: implement login logic
    login_response = LoginResponse(access_token="token")
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=login_response.model_dump()
    )