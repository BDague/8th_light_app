from flask import Flask, render_template, request
from book_parser import BookParser
from book_request_handler import BookAPIRequestHandler
application = Flask(__name__, template_folder='templates', static_folder='static')

@application.route('/', methods=['GET'])
def open():
    return render_template('index.html')

@application.route('/', defaults={'term':None, 'page': 1}, methods=['POST'])
@application.route('/<term>/<page>', methods=['GET'])
def search(term, page):
    if not term:
        term = request.form['term']

    request_handler = BookAPIRequestHandler()
    response = request_handler.request_book_search(term, page)

    if ('items' in response):
        page = int(page)+1
        parser = BookParser()
        books = parser.get_book_data_from_json(response)
        return render_template('index.html', search_word=term, book_data=books, page_number=page)

    elif ('error' in response):
        return response['error']

    else:
        return render_template('index.html', book_data=None)
