from flask import url_for

class Book(object):

    """Data structure to hold information about books"""

    def __init__(self, json):
        keys = ['title', 'publisher', 'imageLinks', 'infoLink']
        info = json['volumeInfo']
        data = {}
        for key in keys:
            try: 
                data[key] = info[key]
            except KeyError:
                data[key] = "Not Listed"
        self.title = data['title']
        if 'authors' in info:
            self.authors = ", ".join(info['authors'])
        else:
            self.authors = 'Not Listed'
        self.publisher = data['publisher']
        try:
            self.picture_link = data['imageLinks']['thumbnail']
        except (KeyError, TypeError) as exception:
            self.picture_link = ""
        self.info_link = data['infoLink']
