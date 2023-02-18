from typing import Union
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    isbn: int
    pages: int
    

class BookCreate(BookBase):
    pass


class BookFetch(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    year_birth: int
    year_passed: Union[int, None]

    
class AuthorCreate(AuthorBase):
    pass


class AuthorFetch(AuthorBase):
    id: int
    books: list[BookFetch]

    class Config:
        orm_mode = True
    