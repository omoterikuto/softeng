from book import Book
from bookshelf import BookShelf

book_shelf = BookShelf()
book_shelf.append_book(Book("Isaac Asimov", "I, Robot"))
book_shelf.append_book(Book("Ray Bradbury", "Fahrenheit 451"))
book_shelf.append_book(Book("Ted Chiang", "Stories of Your Life and Others"))
book_shelf.append_book(
    Book("Philip Kindred Dick", "Do Androids Dream of Electric Sheep?")
)

for book in book_shelf:
    book.print_title()
