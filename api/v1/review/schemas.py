from datetime import datetime
from typing import Any

from pydantic import BaseModel

class ReviewBaseSchema(BaseModel):
    name: str
    content: str
    rating: int
    post_id: int


class ReviewCreateSchema(ReviewBaseSchema):
    pass


class ReviewResponseSchema(ReviewBaseSchema):
    pk: int


class ReviewForPostSchema(BaseModel):
    name: str
    content: str
    rating: int
    post_id: int
    pk: int
    created_at: datetime
