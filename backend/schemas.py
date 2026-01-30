from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str
    level: int
    total_score: int

    class Config:
        from_attributes = True
