from flask import Flask, render_template, url_for
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose')
def choose_book():
    return render_template('choose.html')


if __name__ == '__main__':
    app.run(debug=True)
