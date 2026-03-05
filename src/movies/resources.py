from fastapi import Query
from pydantic import BaseModel
from fastapi.routing import APIRouter
from typing import Optional
from datetime import date
from cinemas.schemas import Cinema

router_m = APIRouter()

@router_m.get("/", tags=["main page"])
def root():
    """Главная страница с основными ссылками"""
    return "Приветствуем на главной странице!"


@router_m.get("/cinemas", tags=["cinemas"])
def get_cinemas() -> list[Cinema]:
    """Переадресация на кинотеатры"""
    return 


@router_m.get("/cinemas/{country}", tags=["country cinemas"])
def get_cinema_country(
        country: str
) -> list[Cinema]:
    """Кинотеатры стран"""
    response = [cinema for cinema in cinemas if cinema['country'] == country]
    return response


@router_m.get("/cinemas/{country}/{location}", tags=["city cinemas"])
def get_cinema_location(
        country: str,
        location: str,
        rating: Optional[float] = Query(None, ge=1.0, le=5.0),
) -> list[Cinema]:
    """Кинотеатры по городам стран"""
    response = [cinema for cinema in cinemas if cinema['country'] == country and cinema['location'] == location]
    return response

@router_m.post("/new_cinema", tags=["add cinema"])
def new_cinema(
        cinema: Cinema,
):
    pass