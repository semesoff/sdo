from pydantic import BaseModel

class UserStatus(BaseModel):
    status: str