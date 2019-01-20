import unittest

class Business_logic_tests(unittest.TestCase):
    def setUp(self):
        self.mock_api_json = {'volumeInfo': 
                {
                    'title': 'Book Title',
                    'authors': ['Au Thor', 'Aut Hor'],
                    'publisher': 'Publisher',
                    'imageLinks': {'thumbnail': ""},
                    'infoLink': 'www.info.com'
                    }
                }

    def test_displays_title(self):
        pass

    def test_displays_author(self):
        pass 

    def test_displays_publisher(self):
        pass 

    def test_displays_ext_info(self):
        pass 

    def test_displays_thumbnail(self):
        pass



if __name__ == '__main__':
    unittest.main()
