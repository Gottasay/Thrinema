from datetime import date
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey

from api.database import Base

class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Cinema(Base, IdMixin):
    __tablename__ = 'cinemas'

    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    rating: Mapped[float] = mapped_column(CheckConstraint(
        'rating >= 0.0 AND rating <= 5.0', name='check_rating'
    ))
    address: Mapped[str]
    halls_amount: Mapped[int]
    opened_at: Mapped[date]

    city: Mapped['City'] = relationship(back_populates='cinema')
    screenings: Mapped[List['Screening']] = relationship(
        back_populates='cinema',
        cascade="all, delete-orphan")


class City(Base, IdMixin):
    __tablename__ = 'cities'

    cinema: Mapped[List['Cinema']] = relationship(
        back_populates='city', cascade='all, delete-orphan')

class Screening(Base):
    __tablename__ = 'screenings'

    movie_id: Mapped[int] = mapped_column(
        ForeignKey('movies.id'), primary_key=True)
    cinema_id: Mapped[int] = mapped_column(
        ForeignKey('cinemas.id'), primary_key=True)
    timestamp: Mapped[date]
    price: Mapped[int]

    movie: Mapped['Movie'] = relationship(
        back_populates='screenings')
    cinema: Mapped['Cinema'] = relationship(
        back_populates='screenings')