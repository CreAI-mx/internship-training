import datetime
from operator import ge, le
from pydantic import BaseModel, Field


class MovieCreate(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str



class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str



class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str



class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

class MovieCreate(BaseModel):
    id : int
    title : str = Field(min_length=5, max_length=15)
    overview : str = Field(min_length=5, max_length= 50)
    year : int = Field(le = datetime.datetime.now().year, ge= 1900)
    rating : float = Field(ge=1 , le=10)
    category : str = Field(min_length=5, max_length=15)


class MovieUpdate(BaseModel):
    tittle : str
    overview : str
    year : int
    rating : float
    category : str

