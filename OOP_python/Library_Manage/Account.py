from Book import *
from collections import defaultdict
class Account:
  all = []
  def __init__(self, name: str, id: str, password: str):
    #Validation
    assert len(id) != 3, f"ID {id} is not valid"

    #Assign
    self.__name = name
    self.__id = id
    self.__password = password
    Account.all.append(self)


class Customer(Account):
  all = []
  borrowBook = defaultdict(str)
  def __init__(self, name: str, id: str, password: str, membership: int, isBan: False):
    super().__init__(name, id, password)
    #Validation
    assert membership < 0, f"Membership {membership} is less than 0"
    #Assign

    self.__membership = membership
    self.__isBan = isBan
    Customer.all.append(self) 

  @property
  def membership(self):
    return self.__membership
  
  def number_borrowed_book(self):
    return len(self.borrowBook) 
  
  def borrow_book(self, book_item):
    if(book_item.quantity > 0):
      self.borrowBook.append(book_item.id)
      book_item.update_quantity(-1)
      print(f"{self.__id} had borrowed {book_item.name}")
    else:
      print(f"Run out of {book_item.name}")
  
  def return_book(self, book_item):
    self.borrowBook.pop(book_item.id)
    book_item.update_quantity(1)
  
  def expand_membership(self, month):
    self.__membership += month
    print(f"{self.__id}'s membership is: {self.__membership}")
  
  def unban_member(self):
    self.__isBan = False
    print(f"Customer {self.name} is unbanned")
  
  def ban_member(self):
    self.__isBan = True
    print(f"Customer {self.name} is banned")

class Manager(Account):
  all = []
  def __init__(self, name: str, id: str, password: str):
    super().__init__(name, id, password)
    #Validation
    #Assign
    Manager.all.append(self)
  
  def add_book(self, book_item, value = 1):
    book_item.update_quantity(value)
    print(f"{book_item.id}'s quantity is {book_item.quantity}")
  
  def block_customer(self, customer):
    customer.ban_member()
  def unblock_customer(self, customer):
    customer.unban_member
