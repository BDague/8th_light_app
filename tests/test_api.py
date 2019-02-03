import unittest
import os
import requests
import json
class TestAPIAssumptions(unittest.TestCase):
    """The reason for this test class is to teach me how the API works. I write and 
    edit tests as I call the API to figure out how the data is structured. Calling
    these tests later enables me to tell if the API changed, so it's useful to keep around

    How this works as of now:
        The API returns an array of  books under the 'items' root key 
        Each object in the items array has a key called 'volumeInfo',
        which contains information related to the projects requirements
    """

    def setUp(self):
        self.api_key = os.environ['GOOG_API_KEY']
        self.url_string = "https://www.googleapis.com/books/v1/volumes?q={}&key={}"

        self.response = requests.get(self.url_string.format('Design', self.api_key))
        self.nonsense_response = requests.get(self.url_string.format('oqwuerjiklfj2u9385983qeiowhfasdkjln2389ewhioffadknsvlejoirghty4390efjowi', self.api_key))

        if not (self.response.ok):
            self.fail("Could not reach the Google Books API")

        self.json = json.loads(self.response.content)
        self.nonsense = json.loads(self.nonsense_response.content)

        self.books = self.json['items']
        self.test_book = self.books[0]
        self.book_info = self.test_book['volumeInfo']



    def test_gets_list_of_books(self):
        self.assertTrue('items' in self.json)

    def test_gets_book_information(self):
        self.assertTrue(self.books)
    
    def test_gets_book_information(self):
        self.assertTrue('volumeInfo' in self.test_book)

    def test_how_to_get_title(self):
        self.assertTrue('title' in self.book_info)

    def test_how_to_get_authors(self):
        self.assertTrue('authors' in self.book_info)

    def test_how_to_get_publisher(self):
        self.assertTrue('publisher' in self.book_info)

    def test_how_to_get_thumbnail(self):
        self.assertTrue('imageLinks' in self.book_info)

    def test_how_to_get_info_link(self):
        self.assertTrue('infoLink' in self.book_info)

    def test_how_responds_to_nonsense(self):
        self.assertFalse('items' in self.nonsense)
