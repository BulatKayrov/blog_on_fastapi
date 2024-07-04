from fastapi import APIRouter, HTTPException, status

from .crud import CRUDReview
from .schemas import ReviewCreateSchema, ReviewResponseSchema
router = APIRouter(prefix="/review", tags=["Reviews"])


@router.post(path="/create", response_model=ReviewResponseSchema)
async def create_review(review: ReviewCreateSchema):
    if review.rating < 0 or review.rating > 5:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rating must be between 0 and 5")
    return await CRUDReview.create(name=review.name, content=review.content, rating=review.rating,
                                   post_id=review.post_id)

