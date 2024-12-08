from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str

class RegisterRequest(BaseModel):
    username: str
    password: str
    group_name: str

class RegisterResponse(BaseModel):
    access_token: str
    role: str