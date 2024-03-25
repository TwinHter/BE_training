import csv

class Item:
  all = []
  pay_rate = 0.8
  def __init__(self, name: str, price: int, quantity=0):
    # Validation
    assert price >= 0, f"Price {price} is not greater than zero"
    assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

    # Assign value
    self.name = name
    self.price = price
    self.quantity = quantity
    #Actions to execute
    Item.all.append(self)

  @classmethod
  def get_from_csv(cls):
    with open('item.csv') as f:
      reader = csv.DictReader(f)
      items = list(reader)
    
    for u in items:
      Item(
        name = u.get('name'), 
        price = float(u.get('price')), 
        quantity = int(u.get('quantity')), 
      )

  @staticmethod
  def is_integer(num):
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate
  
  def __repr__(self):
    return f"{self.__class__.__name__}: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
