from Book import Book
from HistoryBook import HistoryBook
from MusicBook import MusicBook

book1 = Book("ABC", "Dang Nguyen", "Vietnamese", 1000)
book2 = HistoryBook("America's Story", "Rushmore", "English", 2000, 1600)
book3 = MusicBook("The Best Road", "DN", "Japanese", 1500, "Aimer")
print(book1.name)
print(book3.name)
book1.price = 100
print(book1.get_title())

book2.price = 200