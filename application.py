from flask import Flask, render_template, request
from book_parser import BookParser
from book_request_handler import BookAPIRequestHandler
application = Flask(__name__, template_folder='templates', static_folder='static')

@application.route('/', methods=['GET'])
def open():
    return render_template('index.html', book_data=None)

@application.route('/', methods=['POST'])
def search():
    term = request.form['term']
    request_handler = BookAPIRequestHandler()

    response = request_handler.request_book_search(term)

    if ('items' in response):
        parser = BookParser()
        books = parser.get_book_data_from_json(response)
        return render_template('index.html', book_data=books)

    elif ('error' in response):
        return response['error']

    else:
        return render_template('index.html', book_data=None)
