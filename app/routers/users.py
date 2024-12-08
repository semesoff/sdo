from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from http import HTTPStatus

from app.core.check_auth import check_auth
from app.core.jwt_handler import decode_access_token
from app.db.db import get_user_data
from app.schemas.users import UserStatus

router = APIRouter()


def get_user_status(authorization: str = Header(...)) -> JSONResponse:
    check_data = check_auth(authorization)
    if isinstance(check_data, JSONResponse):
        return check_data

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=UserStatus(
            status=check_data['roletype'],
        ).model_dump()
    )


@router.get("/user_status")
async def user_status(data_request: dict = Depends(get_user_status)):
    return data_request

@router.get("/user_data")
async def user_data(authorization: str = Header(...)) -> JSONResponse:
    print(123324234)
    check_data = check_auth(authorization)
    if isinstance(check_data, JSONResponse):
        return check_data

    # Assuming you have a function to get user data from the decoded token
    user_data = get_user_data(check_data['username'])

    if user_data is None:
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={"error": "User not found"}
        )

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=user_data.model_dump()
    )
