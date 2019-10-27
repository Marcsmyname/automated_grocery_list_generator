from mixed import Mixed
#from decimal import Decimal

class Food():
  """Base class for all food in shopping list."""
  #unit for single unit of food
  self.names = ('tsp', 'tbsp', 'cup', 'oz', 'can', ) #increase for all units of measurment
  
  def __init__(self, name='', amount=0):
    self.amount = Mixed(amount)
    self.name = name;
    #14.5 oz. can  
  def __str__(self):
    return amount +  " " + name

  
class 
