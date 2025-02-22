from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr


class UserResponseSchema(UserBase):
    pk: int
    is_admin: bool


class UserCreateSchema(UserBase):
    password: str
    is_admin: bool | None = False


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class PostSchema(BaseModel):
    title: str
    content: str
    pk: int


class UserFullInfoResponseSchema(UserResponseSchema):
    posts: list[PostSchema]


class UserPostSchema(UserBase):
    pk: int
