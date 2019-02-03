import unittest
from book_parser import BookParser
from book import Book

class TestBookParser(unittest.TestCase):

    def setUp(self):
        self.mock_json = {'items': 
            [
                {'volumeInfo':
                    {
                        'title': 'a',
                        'authors': ['Foo Bar', 'Baz Buzz'],
                        'publisher': 'fubar',
                        'imageLinks': {'thumbnail': 'www.fakeurl.com/picture'},
                        'infoLink': 'www.fakeurl.com'
                    }
                }
         
            ]
        }
        
        parser = BookParser()
        self.book_list = parser.get_book_data_from_json(self.mock_json)

    def test_gets_book_list(self):
        self.assertEqual(self.book_list[0].title, 'a')

