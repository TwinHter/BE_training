import csv

class Book:
  __discount = 0.2
  all = []
  def __init__(self, name: str, language: str, id: str, quantity: 0):

    #Validatetion
    assert price > 0, f"Wrong price: {price}"
    assert len(id) != 4, f"Wrond Book ID: {id}"
    assert quantity > 0, f"Wrong quantityy: {quantity}"
    #Assigin value
    self.__name = name
    self.__language = language
    self.__id = id
    self.__quantity = quantity
    Book.all.append(self)

  @property
  def discount(cls):
    return cls.__discount
  @discount.setter
  def discount_changing(cls, value):
    print(f"Update discount of {cls.__class__.__name__} to {value}")
    cls.__discount = value
  # Property
  @property
  def name(self):
    return self.__name
  @property
  def quantity(self):
    return self.__quantity
  @property
  def language(self):
    return self.__language
  @property
  def price(self):
    return self.__price
  @property
  def id(self):
    return self.__id

  def update_quantity(self, value):
    if self.__quantity + value < 0:
      print(f"Wrong update quantity for {self.__name}")
    else:
      self.__quantity += value
      print("Updated")

  def true_price(self):
    print(f"Apply discount {__class__.__discount} and language {self.__language}")
    value = self.__price * __class__.__discount
    if(self.__language == "English" or self.__language == "Vietnamese"):
      value = value * 0.5
    return value
  
  def update_discount(cls, value):
    print("Update Discount")
    cls.__discount = value
  
  def __repr__(self):
    return f"{self.__class__.__name__}: {self.__name}, Price: {self.__price}, Author: {self.__author}, Language: {self.__language}"
  
class HistoryBook(Book):
  __discount = 0.2
  all = []
  def __init__(self, name: str, language: str, price: int, release_year: int):
    super().__init__(
      name, language, price
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

class MusicBook(Book):
  __discount = 0.2
  all = []
  def __init__(self, name: str, language: str, price: int, band: str):
    super().__init__(
      name, language, price
    )
    #Validation

    #Assign value
    self.__band = band
    MusicBook.all.append(self)

  @property
  def band(self):
    return self.__band
  

  def show_content(self):
    print(f"This is a book named {self.__name} about {self.__band}")

  
  