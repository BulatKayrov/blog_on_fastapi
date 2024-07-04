from sqlalchemy import delete, select, Result
from sqlalchemy.orm import selectinload, joinedload

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

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with get_session() as session:
            stmt = select(cls.model).options(joinedload(cls.model.user), selectinload(cls.model.reviews)).filter_by(
                **kwargs)
            post: Result = await session.execute(stmt)
            result = post.scalars().one_or_none()

            if result.reviews:
                result.average_rating = sum(review_rating.rating for review_rating in result.reviews)/len(result.reviews)
            else:
                result.average_rating = 0

            return result
