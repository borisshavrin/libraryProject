from flask import Flask, render_template, url_for, request, redirect

from core.db import session
from library.models import Book
from library.schemas import BookSchema

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose')
def choose_book():
    book_schema = BookSchema(many=True)
    all_books = session.query(Book).all()
    print(all_books)
    dump_data = book_schema.dump(all_books)
    print(dump_data)
    context = {}
    context['books'] = dump_data
    return render_template('choose.html', context=context)


@app.route('/create-book', methods=['POST', 'GET'])
def create_book():
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        qty = request.form['qty']

        book = Book(name=name, desc=desc, qty=qty)
        try:
            session.add(book)
            session.commit()
            return redirect('/')
        except Exception:
            return 'При создании книги произошла ошибка'

    else:
        return render_template('create-book.html')


if __name__ == '__main__':
    app.run(debug=True)
