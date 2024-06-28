from pydantic import BaseModel


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
