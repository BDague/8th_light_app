import requests 
import os

class BookAPIRequestHandler():

    def __init__(self):
        self.url = "https://www.googleapis.com/books/v1/volumes?q={}&key={}&fields=items(volumeInfo(title, authors, publisher, imageLinks, infoLink))"
        self.timeout = 10

    def request_book_search(self, term):
        book_json = requests.Response()
        try:
            formed_url = self.url.format(term, os.environ['GOOG_API_KEY'])
            book_json = requests.get(formed_url, timeout=self.timeout)
            book_json.raise_for_status()

        except requests.exceptions.ConnectionError:
            return {'error': 'Could not reach the Google Books API'}

        
        
        return book_json.json()
