from object import Book, Author

# DATA SOURCE
def get_books():
    return [
        Book(
            title="Some Book",
            author=Author(
                name="Some Name",
                year_birth=1867,
                year_passed=1916,
            ),
            isbn=9784101010038,
            pages=234,
            
        ),
    ]
