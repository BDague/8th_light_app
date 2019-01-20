from flask import Flask, render_template, request
import requests as api_interface
from info_parser import InfoParser
import os
application = Flask(__name__, template_folder='templates')

@application.route('/', methods=['GET'])
def open():
    return render_template('index.html', book_data=None)

@application.route('/', methods=['POST'])
def search():
    formed_url = "https://www.googleapis.com/books/v1/volumes?q={}&key={}".format(request.form['term'], os.environ['GOOG_API_KEY'])
    response = api_interface.get(formed_url)
    parser = InfoParser()
    books = parser.get_book_data_from_json(response.json())
    for book in books:
        print(book.title)
    return render_template('index.html', book_data=books)
