from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from api.database import Base
from sqlalchemy import CheckConstraint

class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Cinema(Base, IdMixin):
    __tablename__ = 'cinema'

    city_id: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(CheckConstraint(
        'rating >= 0.0 AND rating <= 5.0', name='check_rating'
    ),
        nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    halls_amount: Mapped[int] = mapped_column(nullable=False)
    opened_at: Mapped[date]

class Film(Base, IdMixin):
    __tablename__ = 'film'

    description: Mapped[str]
    director: Mapped[str] = mapped_column(nullable=False)
    release_date: Mapped[date] = mapped_column(nullable=False)

class City(Base, IdMixin):
    __tablename__ = 'city'

class Screenings(Base):
    __tablename__ = 'screening'

    cinema_id: Mapped[int] = mapped_column(nullable=False)
    film_id: Mapped[int] = mapped_column(nullable=False)
    timestamp: Mapped[date] = mapped_column(nullable=False)