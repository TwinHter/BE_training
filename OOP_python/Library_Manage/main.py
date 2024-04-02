from Book import *
from Account import *
# Account id's length: 3, Book id's length: 4


manager = Manager('Nguyen', '045')
customer1 = Customer('Quan', '609', 0, False)
customer2 = Customer('Vu', '812', 10, False)

# Add Book
myHistoryBook = dict()
myMusicBook = dict()

def add_history_book(name, language, price, quantity, release_year):
  global myHistoryBook
  tmp = HistoryBook(name, language, price, quantity, release_year)
  myHistoryBook[name] = tmp

def add_music_book(name, language, price, quantity, band):
  global myMusicBook
  tmp = MusicBook(name, language, price, quantity, band)
  myMusicBook[name] = tmp

add_history_book('Lich su DN', 'Vietnamese', 100, 2, 2005)
add_history_book('Napoleon', 'French', 220, 3, 1800)
add_history_book('Holy Relic', 'English', 22000, 5, -100)

add_music_book('Coldplay Theory', 'English', 150, 1, 'Coldplay')
add_music_book('Aimer Anime Queen', 'Japanese', 100, 3, 'Aimer')
add_music_book('Sky oi', 'Vietnamese', 50, 0, 'Son Tung MTP')


# Testing
print(manager)
print(customer1)
customer1.borrow_book(myMusicBook['Aimer Anime Queen'])
print(myMusicBook['Aimer Anime Queen'].quantity)
customer1.borrow_book(myHistoryBook['Napoleon'])
print(customer1.number_borrowed_book())
print(myMusicBook['Aimer Anime Queen'].true_price())
print(myHistoryBook['Lich su DN'].true_price())

manager.block_customer(customer1)
print(customer1)
manager.unblock_customer(customer1)
print(customer1)