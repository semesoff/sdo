from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from http import HTTPStatus
from app.core.jwt_handler import decode_access_token
from app.schemas.users import UserStatus

router = APIRouter()


def get_user_status(authorization: str = Header(...)) -> JSONResponse:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid token format")

    token = authorization[len("Bearer "):]
    print(token)
    # decode user token
    data = decode_access_token(token)
    print(data)
    if isinstance(data, str):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": data}
        )

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=UserStatus(
            status=data['roletype'],
        ).model_dump()
    )


@router.get("/user_status")
async def user_status(data_request: dict = Depends(get_user_status)):
    return data_request