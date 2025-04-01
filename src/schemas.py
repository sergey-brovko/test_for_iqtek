from pydantic import BaseModel


class User(BaseModel):
    full_name: str


class UserRepository(User):
    id: int

    class Config:
        from_attributes = True
