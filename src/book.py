class Book(object):

    """Data structure to hold information about books"""

    def __init__(self, json): 
        info = json['volumeInfo']
        self.title = info['title']
        self.authors = info['authors']
        try:
            self.publisher = info['publisher']
        except KeyError:
            self.publisher = info['publishedDate']
        self.picture_link = info['imageLinks']
        self.info_link = info['infoLink']
