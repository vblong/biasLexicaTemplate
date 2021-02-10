# My own Article class that only stores data that I consider important
class IArticle:
    authors = []
    title = ""
    text = ""
    categories = []
    url = ""
    date = None

    def __init__(self, authors = [], title = "", text = "", categories = [], url = "", date = None):
        self.authors    = authors
        self.title      = title
        self.text       = text
        self.categories = categories
        self.url        = url
        self.date       = date

    def set_authors(self, authors):
        self.authors = authors

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_categories(self, categories):
        self.categories = categories

    def set_url(self, url):
        self.url = url

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return f'IArticle(Title:{self.title},Authors:{self.authors},Published:{self.date})'