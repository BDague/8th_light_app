import unittest
from book_request_handler import BookAPIRequestHandler

class TestRequestHandler(unittest.TestCase):

    def setUp(self):
        self.requester = BookAPIRequestHandler()

    def test_gets_books_normally(self):
        data = self.requester.request_book_search('flowers')
        self.assertTrue('items' in data)

    def test_handles_bad_connection(self):
        #this url has the format call applied to it, needs the brackets!
        self.requester.url = 'http://localhost:2012/ho{}pefullyf{}akeurl'
        data = self.requester.request_book_search('flowers')
        self.assertEqual(data, {'error': 'Could not reach the Google Books API'})
