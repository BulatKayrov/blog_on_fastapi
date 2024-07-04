from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import BaseCRUDModel, User
from models import get_session


class UserCRUDModel(BaseCRUDModel):
    model = User

    @classmethod
    async def get_user_by_email(cls, email):
        async with get_session() as session:
            stmt = select(cls.model).where(cls.model.email == email)
            res = await session.execute(stmt)
            return res.scalars().first()

    @classmethod
    async def create_user(cls, email, password, first_name=None, last_name=None, is_admin=False):
        async with get_session() as session:
            user = cls.model(email=email, password=password, first_name=first_name, last_name=last_name,
                             is_admin=is_admin)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    @classmethod
    async def find_full_info_by(cls, **kwargs):
        async with get_session() as session:
            stmt = select(cls.model).options(selectinload(cls.model.posts)).filter_by(**kwargs)
            print(stmt)
            res = await session.execute(stmt)
            return res.scalars().first()
