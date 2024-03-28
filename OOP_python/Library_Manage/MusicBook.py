from Book import Book

class MusicBook(Book):
  __discount = 0.2
  all = []
  def __init__(self, name: str, author: str, language: str, price: int, band: str):
    super().__init__(
      name, author, language, price
    )
    #Validation

    #Assign value
    self.__band = band
    MusicBook.all.append(self)

  @property
  def band(self):
    return self.__band
  

  def show_content(self):
    print(f"The book is {self._Book__name} of {self._Book__author}. It is about {self.__band}.")

  
  