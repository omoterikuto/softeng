class Book:
    _author: str
    _title: str
    _pages: int

    def __init__(self, author, title):
        self._author = author
        self._title = title

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._pages = pages

    def print_author(self):
        print(self.author)

    def print_title(self):
        print(self.title)

    def print_pages(self):
        print(self.pages)

    def print_detail(self):
        self.print_author()
        self.print_title()
        self.print_pages()


if __name__ == "__main__":
    b = Book("夏目漱石", "坊っちゃん")
    b.pages = 500
    b.print_detail()
    b2 = Book("Charles Dickens", "A Tale of Two Cities")
    b2.pages = 400
    b2.print_detail()
