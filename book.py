from flask import url_for

class Book(object):

    """Data structure to hold information about books"""

    def __init__(self, json):
        keys = ['title', 'authors', 'publisher', 'imageLinks', 'infoLink']
        info = json['volumeInfo']
        data = {}
        for key in keys:
            try: 
                data[key] = info[key]
            except KeyError:
                data[key] = "Not Listed"
        self.title = data['title']
        self.authors = data['authors']
        self.publisher = data['publisher']
        try:
            self.picture_link = data['imageLinks']['thumbnail']
        except (KeyError, TypeError) as exception:
            self.picture_link = url_for('static',  filename='default_book.png')
        self.info_link = data['infoLink']
