from book import Book

class BookParser(object):

    """Offers methods to collect data from the books as passed ot it by the 
    Google books API"""

    def __init__(self):
        pass
        

    def get_book_data_from_json(self, data):
        """
        data: json encoded data, should have a list in it with the key 'items'
        return: list of book objects
        """
        items = data['items']
        books = []
        for book_data in items:
            books.append(Book(book_data))

        return books


