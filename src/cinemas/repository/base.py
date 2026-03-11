from sqlalchemy import select
from src.cinemas.database import async_session_maker
from src.cinemas.schemas import Cinema
from src.cinemas.models import Cinema as CinemaModel


class BaseRep:
    model = None

    @classmethod
    async def find_by_name(cls, model_name: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(name=model_name)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_user(cls):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none() # Либо один объект либо ничего

    @classmethod
    async def get_all_cinemas(cls, **filter_by):
        async with async_session_maker() as session:
            request = select(cls.model).filter_by(**filter_by)
            response = await session.execute(request)
            return response.scalars().all()