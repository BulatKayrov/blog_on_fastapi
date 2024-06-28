from fastapi import APIRouter

from .user.views import router as user_router
from .post.views import router as post_route

router = APIRouter()
router.include_router(user_router)
router.include_router(post_route)