from datetime import timedelta

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from app.config.config import init_config
from app.core.jwt_handler import create_access_token
from app.db.db import validate_user, validate_user
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()
cfg = init_config()['jwt']


@router.post("/login")
async def login(request: LoginRequest):
    print(f"Received login request: {request}")
    user_data = validate_user(
        username=request.username,
        password=request.password
    )
    print(user_data)
    # if already exists in db
    if not user_data:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": "User already exists"}
        )

    # generate jwt token & more
    user_token = create_access_token(user_data, timedelta(seconds=cfg['expires_in']))
    login_response = LoginResponse(access_token=user_token)
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=login_response.model_dump()
    )

