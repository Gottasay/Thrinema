from fastapi import Query
from pydantic import BaseModel
from fastapi.routing import APIRouter
from typing import Optional
from datetime import date
from api.schemas import Cinema

router = APIRouter()

cinemas = [
    {'id': 1, 'country': 'USA', 'location': 'New York', 'name': 'Lazy Bird', 'rating': 4.5, 'created_at': date.today()},
    {'id': 2, 'country': 'Russia', 'location': 'Moscow', 'name': 'Белый бумер', 'rating': 3.9, 'created_at': date(2007, 11, 5)},
    {'id': 3, 'country': 'Belarus', 'location': 'Minsk', 'name': 'Бацка', 'rating': 4.1, 'created_at': date(2015, 4, 30)},
]

@router.get("/", tags=["main page"])
def root():
    """Главная страница с основными ссылками"""
    return "Приветствуем на главной странице!"


@router.get("/cinemas", tags=["cinemas"])
def get_cinemas() -> list[Cinema]:
    """Переадресация на кинотеатры"""
    return cinemas


@router.get("/cinemas/{country}", tags=["country cinemas"])
def get_cinema_country(
        country: str
) -> list[Cinema]:
    """Кинотеатры стран"""
    response = [cinema for cinema in cinemas if cinema['country'] == country]
    return response


@router.get("/cinemas/{country}/{location}", tags=["city cinemas"])
def get_cinema_location(
        country: str,
        location: str,
        rating: Optional[float] = Query(None, ge=1.0, le=5.0),
) -> list[Cinema]:
    """Кинотеатры по городам стран"""
    response = [cinema for cinema in cinemas if cinema['country'] == country and cinema['location'] == location]
    return response

@router.post("/new_cinema", tags=["add cinema"])
def new_cinema(
        cinema: Cinema,
):
    pass