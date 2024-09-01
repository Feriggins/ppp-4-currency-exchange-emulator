class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  #add magic methods here
  def __repr__(self):
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return f"{self.value:.2f} {self.unit}"
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return self.__repr__()
  
  def __add__(self, other):
        if isinstance(other, Currency):
            # Convert other currency to self's unit before adding
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            # Treat other as USD and convert it to self's unit before adding
            usd_value = other  # other is treated as USD
            usd_value_in_self_unit = usd_value * Currency.currencies[self.unit] / Currency.currencies['USD']
            return Currency(self.value + usd_value_in_self_unit, self.unit)
        else:
            return NotImplemented

  def __iadd__(self, other):
      # In-place addition using __add__
      result = self.__add__(other)
      if isinstance(result, Currency):
          self.value = result.value
          self.unit = result.unit
      return self

  def __radd__(self, other):
      # Handles reversed addition when the first operand is not a Currency
      if isinstance(other, (int, float)):
          # Treat other as USD and return result in USD
          self_value_in_usd = self.value / Currency.currencies[self.unit]
          return Currency(self_value_in_usd + other, 'USD')
      else:
          return NotImplemented

  def __sub__(self, other):
      if isinstance(other, Currency):
          # Convert other currency to self's unit before subtracting
          other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
          return Currency(self.value - other_value_in_self_unit, self.unit)
      elif isinstance(other, (int, float)):
          # Treat other as USD and convert it to self's unit before subtracting
          usd_value = other  # other is treated as USD
          usd_value_in_self_unit = usd_value * Currency.currencies[self.unit] / Currency.currencies['USD']
          return Currency(self.value - usd_value_in_self_unit, self.unit)
      else:
          return NotImplemented

  def __isub__(self, other):
      # In-place subtraction using __sub__
      result = self.__sub__(other)
      if isinstance(result, Currency):
          self.value = result.value
          self.unit = result.unit
      return self

  def __rsub__(self, other):
      # Handles reversed subtraction when the first operand is not a Currency
      if isinstance(other, (int, float)):
          # Treat other as USD and subtract self's value from it
          self_value_in_usd = self.value / Currency.currencies[self.unit]
          return Currency(other - self_value_in_usd, 'USD')
      else:
          return NotImplemented
      

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
