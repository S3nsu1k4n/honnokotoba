import strawberry
from typing import List
from object import Book
import fetch


# RESOLVER
@strawberry.type
class Query:
    @strawberry.field
    def books() -> List[Book]:
        return fetch.get_books()
