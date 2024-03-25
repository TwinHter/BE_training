from item import Item

class Phone(Item):
  def __init__(self, name: str, price: int, quantity = 0, broken_phones = 0):
    # Call to super function to have acess to attributes/ methods of parent class
    super().__init__(
      name, price, quantity
    )
    # Validation
    assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero"

    # Assign value
    self.broken_phones = broken_phones