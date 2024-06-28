from sqlalchemy import select, insert

from .db_helper import get_session


class BaseCRUDModel:  # CRUD
    model = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with get_session() as session:
            stmt = select(cls.model).filter_by(**kwargs)
            res = await session.execute(stmt)
            return res.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with get_session() as session:
            stmt = select(cls.model).filter_by(**kwargs)
            result = await session.execute(stmt)
            return result.scalars().one_or_none()

    @classmethod
    async def create(cls, **kwargs):
        async with get_session() as session:
            stmt = cls.model(**kwargs)
            session.add(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def update(cls, **kwargs):
        async with get_session() as session:
            stmt = cls.model.update().where(cls.model.c.id == kwargs['id']).values(**kwargs)
            await session.execute(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def delete(cls, **kwargs):
        async with get_session() as session:
            stmt = cls.model.delete().where(cls.model.pk == kwargs['pk'])
            await session.execute(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def find_by(cls, **kwargs):
        async with get_session() as session:
            stmt = select(cls.model).filter_by(**kwargs)
            res = await session.execute(stmt)
            return res.scalars().first()
