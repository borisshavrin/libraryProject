from sqlalchemy import Integer, Column, String, Text

from core.db import Base


class Book(Base):
    __tablename__ = 'library_books'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=128), nullable=False)     # blank=False
    desc = Column(Text, nullable=False)
    qty = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.id
