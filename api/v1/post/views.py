from fastapi import APIRouter, Depends, HTTPException

from api.v1.user.utils import get_user_by_token
from .schemas import PostCreateSchema, PostUpdateSchema, PostResponseSchema
from .crud import PostCRUDModel

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/all", response_model=list[PostResponseSchema])
async def get_all_posts():
    return await PostCRUDModel.find_all()


@router.post("/create")
async def create_post(post: PostCreateSchema, user=Depends(get_user_by_token)):
    return await PostCRUDModel.create(title=post.title, content=post.content, user_id=user.pk)


@router.delete("/delete/{pk}")
async def delete_post(pk: int, user=Depends(get_user_by_token)):
    return await PostCRUDModel.delete(pk=pk, user_id=user.pk)
