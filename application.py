from flask import Flask, render_template, request
import requests as api_interface
from book_parser import BookParser
import os
application = Flask(__name__, template_folder='templates', static_folder='static')

@application.route('/', methods=['GET'])
def open():
    return render_template('index.html', book_data=None)

@application.route('/', methods=['POST'])
def search():
    formed_url = "https://www.googleapis.com/books/v1/volumes?q={}&key={}".format(request.form['term'], os.environ['GOOG_API_KEY'])
    response = api_interface.get(formed_url)
    parser = BookParser()
    books = parser.get_book_data_from_json(response.json())
    return render_template('index.html', book_data=books)
