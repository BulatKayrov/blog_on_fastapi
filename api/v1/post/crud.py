from sqlalchemy import delete

from models import BaseCRUDModel, Post, get_session


class PostCRUDModel(BaseCRUDModel):
    model = Post

    @classmethod
    async def delete(cls, **kwargs):
        async with get_session() as session:
            post = delete(cls.model).filter_by(**kwargs)
            await session.execute(post)
            await session.commit()
            return None
