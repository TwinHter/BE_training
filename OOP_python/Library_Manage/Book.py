import csv

class Book:
  __discount = 0.2
  all = []
  def __init__(self, name: str, author: str, language: str, price: int):

    #Validatetion
    assert price > 0, f"Wrong price: {price}"

    #Assigin value
    self.__name = name
    self.__author = author
    self.__language = language
    self.__price = price

    Book.all.append(self)
  
  @classmethod
  def get_from_csv(cls):
    with open('book.csv') as f:
      reader = csv.DictReader(f)
      books = list(reader)
    
    for u in books:
      Book(
        name = u.get('name'),
        author =  int(u.get('author')),
        language = u.get('language'),
        price = int(u.get('price'))
      )

  
  @property
  def discount(cls):
    return cls.__discount
  @discount.setter
  def discount_changing(cls, value):
    print(f"Update discount of {cls.__class__.__name__} to {value}")
    cls.__discount = value
  @property
  def name(self):
    return self.__name
  @property
  def author(self):
    return self.__author
  @property
  def language(self):
    return self.__language
  
  @property
  def price(self):
    return self.__price
  @price.setter
  def price(self, value):
    print(f"Update Price of {self.__name} to {value}")
    self.__price = value

  def get_title(self):
    return self.__name
  
  def true_price(self):
    value = self.__price * __class__.__discount
    if(self.__language == "English" or self.__language == "Vietnamese"):
      value = value * 0.5
    return value
  
  def __repr__(self):
    return f"{self.__class__.__name__}: {self.__name}, Price: {self.__price}, Author: {self.__author}, Language: {self.__language}"


    