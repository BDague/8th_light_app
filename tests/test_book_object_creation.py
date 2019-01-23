import unittest
from src.book import Book

class book_tester(unittest.TestCase):
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

    def test_gets_title(self):
        self.assertEqual(self.book.title, self.mock_api_json['volumeInfo']['title'])

    def test_gets_author(self): 
        self.assertEqual(self.book.authors, self.mock_api_json['volumeInfo']['authors'])

    def test_gets_publisher(self):
        self.assertEqual(self.book.publisher, self.mock_api_json['volumeInfo']['publisher'])

    def test_gets_ext_info(self):
        self.assertEqual(self.book.picture_link, self.mock_api_json['volumeInfo']['imageLinks']['thumbnail'])
         
    def test_gets_thumbnail(self):
        self.assertEqual(self.book.info_link, self.mock_api_json['volumeInfo']['infoLink'])



if __name__ == '__main__':
    unittest.main()
