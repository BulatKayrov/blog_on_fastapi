from fastapi import APIRouter, Depends, status

from api.v1.user.utils import get_user_by_token
from .crud import PostCRUDModel
from .schemas import PostCreateSchema, PostResponseSchema, PostFindByPKResponseSchema

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get(path="/all", response_model=list[PostResponseSchema])
async def get_all_posts(offset: int | None = None, limit: int | None = None):
    return await PostCRUDModel.find_all(offset=offset, limit=limit)


@router.post(path="/create", response_model=PostResponseSchema)
async def create_post(post: PostCreateSchema, user=Depends(get_user_by_token)):
    return await PostCRUDModel.create(title=post.title, content=post.content, user_id=user.pk)


@router.delete(path="/delete/{pk}", status_code=status.HTTP_200_OK)
async def delete_post(pk: int, user=Depends(get_user_by_token)):
    return await PostCRUDModel.delete(pk=pk, user_id=user.pk)


@router.get(path='/{pk}', response_model=PostFindByPKResponseSchema)
async def get_post(pk: int):
    result = await PostCRUDModel.find_one_or_none(pk=pk)
    return result
