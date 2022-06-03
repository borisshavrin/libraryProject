from app import ma


class BookSchema(ma.Schema):
    class Meta:
        fields = ('name', 'desc', 'qty')


book_schema = BookSchema.query.all()
books_schema = BookSchema.query.all(many=True)
