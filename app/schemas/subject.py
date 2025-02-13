from pydantic import BaseModel

class SubjectInfo(BaseModel):
    id: int
    name: str
    grade: float | None