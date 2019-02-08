import requests 
import os

class BookAPIRequestHandler():
    
    def __init__(self):
        self.url = "https://www.googleapis.com/books/v1/volumes?q={}&key={}&fields=items(volumeInfo(title, authors, publisher, imageLinks, infoLink))&startIndex={}"
        self.timeout = 10

    def request_book_search(self, term, page=0):
        """Runs a query against the API 
        term: the search term, entered by the user  
        page: used in the paginiation of the data

        returns: data from query, as json if succeeds, error json in other cases
        """

        book_json = requests.Response()
        try:
            if term:
                formed_url = self.url.format(term, os.environ['GOOG_API_KEY'], page)
                book_json = requests.get(formed_url, timeout=self.timeout)
                book_json.raise_for_status()
            else:
                return {}

        except requests.exceptions.ConnectionError:
            return {'error': 'Could not reach the Google Books API'}

        
        
        return book_json.json()
