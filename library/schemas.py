from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from library.models import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        fields = ('name', 'desc', 'qty', 'id', 'is_active')
        include_relationships = True
        load_instance = True
