from sqlalchemy import Integer, Column, String, Text, Boolean

from core.db import Base


class Book(Base):
    __tablename__ = 'library_books'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=128), nullable=False)     # blank=False
    desc = Column(Text, nullable=False)
    qty = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        return '<Book %r>' % self.id
