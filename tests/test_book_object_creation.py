import unittest
from flask import Flask, session
from book import Book

class TestBookGenereatesCorrectly(unittest.TestCase):
    def setUp(self):
        self.mock_api_json = { 'volumeInfo': 
                    {
                        'title': 'Book Title',
                        'authors': ['Au Thor', 'Aut Hor'],
                        'publisher': 'Publisher',
                        'imageLinks': {'thumbnail': ""},
                        'infoLink': 'www.info.com'
                        }
                    }
        
        self.book = Book(self.mock_api_json)

        self.mock_blank_json = { 'volumeInfo': {}}
        self.blank_book = Book(self.mock_blank_json)

    def test_gets_title(self):
        self.assertEqual(self.book.title, "Book Title")

    def test_gets_author(self): 
        self.assertEqual(self.book.authors, "Au Thor, Aut Hor")

    def test_gets_publisher(self):
        self.assertEqual(self.book.publisher, "Publisher")

    def test_gets_thumbnail(self):
        self.assertEqual(self.book.picture_link, "")
         
    def test_gets_info_link(self):
        self.assertEqual(self.book.info_link, "www.info.com")

    def test_default_author(self):
        self.assertEqual(self.blank_book.authors, 'Not Listed')

    def test_default_title(self):
        self.assertEqual(self.blank_book.title, 'Not Listed')

    def test_default_publisher(self):
        self.assertEqual(self.blank_book.publisher, 'Not Listed')

    def test_default_info_link(self):
        self.assertEqual(self.blank_book.info_link, 'Not Listed')

    def test_uses_default_image(self):
        self.assertEqual(self.blank_book.picture_link, "")




if __name__ == '__main__':
    unittest.main()
