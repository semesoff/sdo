from datetime import timedelta

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from app.config.config import init_config
from app.core.jwt_handler import create_access_token
from app.db.db import validate_user, add_user
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from app.schemas.jwt_token import TokenData

router = APIRouter()
cfg = init_config()['jwt']


@router.post("/login")
async def login(request: LoginRequest):
    user_data = validate_user(
        username=request.username,
        password=request.password
    )
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


@router.post("/register")
async def register(request: RegisterRequest):
    user_data = validate_user(
        username=request.username,
        password=request.password
    )
    # if not exists in db
    if user_data:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": "User already exists"}
        )

    # add user to db
    res_data = add_user(request)
    if isinstance(res_data, str):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": "User not added."}
        )

    jwt_data = {
        "username": res_data.get('username'),
        "roletype": res_data.get('roletype'),
        "studygroup": res_data.get('studygroup')
    }

    # generate jwt token & more
    user_token = create_access_token(jwt_data, timedelta(seconds=cfg['expires_in']))
    login_response = RegisterResponse(
        access_token=user_token,
        role=res_data.get('roletype', 'default_role'),
    )
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=login_response.model_dump()
    )