from pydantic import BaseModel, EmailStr

from api.v1.review.schemas import ReviewForPostSchema


class PostBaseSchema(BaseModel):
    title: str
    content: str


class PostCreateSchema(PostBaseSchema):
    pass


class PostUpdateSchema(PostBaseSchema):
    title: str | None = None
    content: str | None = None


class PostResponseSchema(PostBaseSchema):
    pk: int
    user_id: int


class PostSchemaByUser(PostBaseSchema):
    pk: int


class UserPostSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    pk: int


class PostFindByPKResponseSchema(PostBaseSchema):
    pk: int
    user: UserPostSchema | None
    reviews: list[ReviewForPostSchema] | None
    average_rating: float | int
