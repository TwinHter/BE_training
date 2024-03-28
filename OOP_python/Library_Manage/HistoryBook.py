from Book import Book

class HistoryBook(Book):
  __discount = 0.2
  all = []
  def __init__(self, name: str, author: str, language: str, price: int, release_year: int):
    super().__init__(
      name, author, language, price
    )
    #Validation
    assert release_year <= 2024, f"Wrong release year format: {release_year}"

    #Assign value
    self.__release_year = release_year
    HistoryBook.all.append(self)
  
  @property
  def release_year(self):
    return self.__release_year
  
  def historic_rate(self):
    value = self.__release_year
    if(value < 0): print("TCN")
    elif(value < 1500): print("Before 15th century")
    else: print("Not old enough")
  
