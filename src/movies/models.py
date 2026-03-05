from datetime import date
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from movies.models import *
from movies.database import Base
from src.cinemas.models import IdMixin

class Movie(Base, IdMixin):
    __tablename__ = 'movies'

    description: Mapped[str]
    release_date: Mapped[date] = mapped_column(nullable=False)

    genre: Mapped[List['Genre']] = relationship(
        back_populates='movie',
        secondary='movie_genre'
    )
    director: Mapped[List['Director']] = relationship(back_populates='movie', secondary='movie_director')
    screenings: Mapped[List['Screening']] = relationship(
        back_populates='movie',
        cascade="all, delete-orphan")

class Genre(Base, IdMixin):
    __tablename__ = 'genres'

    movie: Mapped[List['Movie']] = relationship(
        back_populates='genre',
        secondary='movie_genre'
    )

class Director(Base, IdMixin):
    __tablename__ = 'directors'

    movie: Mapped[List['Movie']] = relationship(back_populates='director', secondary='movie_director')

class MovieGenre(Base):
    __tablename__ = 'movie_genre'

    movie_id: Mapped[int] = mapped_column(
        ForeignKey('movies.id'), primary_key=True)
    genre_id: Mapped[int] = mapped_column(
        ForeignKey('genres.id'), primary_key=True)

class MovieDirector(Base):
    __tablename__ = 'movie_director'

    movie_id: Mapped[int] = mapped_column(
        ForeignKey('movies.id'), primary_key=True)
    director_id: Mapped[int] = mapped_column(
        ForeignKey('directors.id'), primary_key=True)