from database import SessionLocal, engine
from sqlalchemy.orm import Session

import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


for db in get_db():
    crud.add_author(db=db, author=schemas.AuthorCreate(name="夏目漱石", year_birth=1867, year_passed=1916))
    crud.add_author(db=db, author=schemas.AuthorCreate(name="沢木耕太郎", year_birth=1947, year_passed=None))
    crud.add_author(db=db, author=schemas.AuthorCreate(name="山崎豊子", year_birth=1924, year_passed=2013))
    
    crud.add_book(db=db, book=schemas.BookCreate(title="坊っちゃん", isbn=9784101010038, pages=234), author_name="夏目漱石")
    crud.add_book(db=db, book=schemas.BookCreate(title="こころ", isbn=9784101010037, pages=378), author_name="夏目漱石")
    crud.add_book(db=db, book=schemas.BookCreate(title="深夜特急１", isbn=9784101235288, pages=270), author_name="沢木耕太郎")
    crud.add_book(db=db, book=schemas.BookCreate(title="白い巨塔１", isbn=9784101104331, pages=422), author_name="山崎豊子")
    crud.add_book(db=db, book=schemas.BookCreate(title="花のれん", isbn=9784101104034, pages=327), author_name="山崎豊子")
    