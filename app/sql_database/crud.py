from sqlalchemy.orm import Session

import models, schemas


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_author_by_name(db: Session, author_name: str):
    return db.query(models.Author).filter(models.Author.name == author_name).first()


def get_book_by_name(db: Session, book_title: str):
    return db.query(models.Book).filter(models.Book.title == book_title).first()


def get_book_by_isbn(db: Session, isbn: int):
    return db.query(models.Book).filter(models.Book.isbn == isbn).first()


def add_book(db: Session, book: schemas.BookCreate, author_name: str):
    author = get_author_by_name(db=db, author_name=author_name)
    if author is None:
        print(f"Author {author.name} does not exist yet")
        return
    book_by_isbn = get_book_by_isbn(db=db, isbn=book.isbn)
    if book_by_isbn is not None:
        print(f"ISBN {book.isbn} with book title {book_by_isbn.title} already exists")
        return
    db_book = models.Book(**book.dict(), author_id=author.id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def add_author(db: Session, author: schemas.AuthorCreate):
    author_by_name = get_author_by_name(db=db, author_name=author.name)
    if author_by_name is not None:
        print(f"Author {author_by_name.name} already exists")
        return
    
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
