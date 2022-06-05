import pytest

from app import app
from library.models import Book

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL_TEST = 'sqlite:///test.db'

engine_test = create_engine(SQLALCHEMY_DATABASE_URL_TEST, connect_args={'check_same_thread': False}, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
Base = declarative_base()
session_test = SessionLocal()

client = app.test_client()


def test_request_example():
    response = client.get('/')
    assert response.status_code == 200


def test_new_book():
    name = 'Маленький принц'
    author = 'Экзюпери'
    desc = 'Отличная книга'
    qty = 15
    is_active = True

    book_test = Book(name=name, author=author, desc=desc, qty=qty, is_active=is_active)
    session_test.add(book_test)
    session_test.commit()

    assert book_test.name == name
    assert book_test.author == author
    assert book_test.desc == desc
    assert book_test.qty == qty
    assert book_test.is_active == is_active


if __name__ == '__main__':
    pytest.main()
