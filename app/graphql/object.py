import strawberry


@strawberry.type
class Author:
    name: str
    year_birth: int
    year_passed: int
    

@strawberry.type
class Book:
    title: str
    author: Author
    isbn: int
    pages: int
