from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    roletype: str
    studygroup: str
    form_education: str
    faculty: str

class UserStatus(BaseModel):
    status: str