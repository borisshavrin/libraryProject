from flask import Flask, render_template, url_for, request, redirect

from core.db import session
from library.models import Book
from library.schemas import BookSchema

app = Flask(__name__)


@app.route('/')
def index():
    context = {}
    context['title'] = 'Главная страница'
    return render_template('index.html', context=context)


@app.route('/choose')
def choose_book():
    context = {}
    context['title'] = 'Выбрать книгу'

    book_schema = BookSchema(many=True)
    books_is_active = session.query(Book).filter(Book.is_active==True)
    dump_data = book_schema.dump(books_is_active)
    authors = session.query(Book.author).distinct().all()
    context['books'] = dump_data
    context['authors'] = authors

    return render_template('choose.html', context=context)


@app.route('/create-book', methods=['POST', 'GET'])
def create_book():
    context = {}
    context['title'] = 'Добавление книги'
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        qty = request.form['qty']
        author = request.form['author']
        is_active = False
        if qty and int(qty) > 0:
            is_active = True
        else:
            qty = 0
        print(author)
        book = Book(name=name, author=author, desc=desc, qty=qty, is_active=is_active)
        try:
            session.add(book)
            session.commit()
            return redirect('/')
        except Exception:
            return 'При создании книги произошла ошибка'

    else:
        return render_template('create-book.html', context=context)


@app.route('/take-book/<int:id>')
def take_book(id):
    book_by_id = session.query(Book).filter_by(id=id).one()
    book_by_id.qty -= 1
    if book_by_id.qty == 0:
        book_by_id.is_active = False
    try:
        session.add(book_by_id)
        session.commit()
        return redirect('/')
    except Exception:
        return 'При изменении кол-ва книги произошла ошибка'


@app.route('/manage-book')
def manage_book():
    context = {}

    book_schema = BookSchema(many=True)
    all_books = session.query(Book).all()
    dump_data = book_schema.dump(all_books)

    context['books'] = dump_data
    return render_template('manage-book.html', context=context)


@app.route('/update-desc/<int:id>', methods=['POST', 'GET'])
def update_desc_id(id):
    context = {}
    book_by_id = session.query(Book).filter_by(id=id).one()
    if request.method == 'GET':
        book_schema = BookSchema()
        dump_data = book_schema.dump(book_by_id)
        context['book'] = dump_data
        context['title'] = 'Изменить описание'
        """Переход к формам"""
        return render_template('update-book.html', context=context)

    elif request.method == 'POST':
        """Получили форму"""
        new_desc = request.form['desc']
        book_by_id = session.query(Book).filter_by(id=id).one()
        book_by_id.desc = new_desc

    try:
        session.add(book_by_id)
        session.commit()
        return redirect('/')
    except Exception:
        return 'При изменении кол-ва книги произошла ошибка'


@app.route('/delete-book/<int:id>')
def delete_book(id):
    book_by_id = session.query(Book).filter_by(id=id).one()
    try:
        session.delete(book_by_id)
        session.commit()
    except Exception:
        return 'Ошибка при попытке удаления книги'
    else:
        return redirect('/')


@app.route('/filter-by-author/<author>')
def filter_by_author(author):
    context = {}
    book_schema = BookSchema(many=True)
    books_by_author = session.query(Book).filter(Book.author==author)
    dump_data = book_schema.dump(books_by_author)

    context['books'] = dump_data
    return render_template('choose.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
