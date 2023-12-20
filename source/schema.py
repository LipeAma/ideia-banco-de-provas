from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    age: int
    password: str


class UserPublic(BaseModel):
    username: str
    email: str


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserDB]
