from mixed import Mixed
#from decimal import Decimal

#will amount be required?
class Food():
  """Base class for all food in shopping list."""
  #aisle where food is located in store
  self.aisle = ''
  
  def __init__(self, amount=0, name=''):
    self.amount = Mixed(amount)
    self.name = name;
    #14.5 oz. can  
    #add aritmetic operations
    
  def __str__(self):
    if not name:
      return amount
    else:
      return amount +  " " + name

#foods need to be modified, unit of measure or name
#meats
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BeefChuckRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'beef chuck roast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundBeef(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground beef'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GroundItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground italian sausage'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'italian sausage'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class PorkShoulder(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'pork shoulder'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Bacon(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bacon'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GroundTurkey(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground turkey'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HamSteak(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bone in ham bone steak'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenThighs(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'chicken thighs'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SerloinTipRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'sliced & fat trimmed boneless sirloin tip roast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  #Dairy

class AmericanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HeavyCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Milk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class HeavyWhippingCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ParmeseanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'parmesean cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Butter(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butter'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class EvaporatedMilk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'evaporated milk'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CreamCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cream cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SourCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'sour cream'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class MontereyJackCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'monterey jack cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CheddarCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cheddar cheese'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
'''
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food


class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = 'meat'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    '''
#spices and sauces, veggies, pasta
#Non-food items
class FreezerBag(Food):
  def __init__(self, amount=1'):
    Super().__init__(amount)
    self.food = 'freezer bag'
    self.category = 'non-food'
               
  def __str__(self):
    return Super.__str__() + " " + self.food

'''  self.chili_spiced_beef_and_carrots = ['1 lb baby carrots', '1 lb baby carrots','',]
self.tuscan_steak_and_green_peppers = [ 'frozen bell peppers','onion', '14.5 oz DICED tomatoes']
self.beef_and_cabbage_soup = ['small cabage', 'onion', 'carrots', '14.5 oz DICED tomatoes']
self.sloppy_joes = ['onion','red bell pepper', '15 OZ. tomato Sauce']
self.chicken_spinach_alfredo = ['spinach']
self.chicken_tikka_masala = ['15 OZ. tomato sauce','15 OZ. tomato sauce']
self.shredded_chicken_fajitas = ['red bell pepper']
self.chicken_cordon_bleu_casserole = ['extra wide egg noodles', 'italian bread crumbs']
self.chicken_and_sausage_orzo =['8oz._tomatoe SAUCE', 'orzo']
self.italian_sausage_rigatoni = ['14.5 oz DICED tomatoes','14.5 oz DICED tomatoes', 'onion', '4.5 cups rigatoni']
self.gvb_soup_turkey = ['carrots', 'zucchini',]
self.tuscaan_torellini_soup = ['24oz pasta sauce', 'cannellini beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini']
self.white_chicken_chili = ['salsa verde', 'cannellini beans', 'cannellini beans', ]
self.ranch_popcorn_chicken = ['egg', 'cornflakes',]
self.cheesy_chicken_veggie_casserole = ['green onions', 'shredded cheddar', 'ritz', ]
self.pulled_pork = ['onion',]
self.suasage_and_peppers =['rainbow peppers','rainbow peppers', 'rainbow peppers', 'onion']
self.potatoe_corn_chowder = ['red potatoes', 'red potatoes', 'red potatoes', 'celery']
self.jalepeno_and_bacon = ['elbow macoroni', 'cheddar cheese', 'jalepeno', 'onions']
self.indian_butter_chicken = [' '15oz tomatoe sauce', '15oz tomatoe sauce']', 'butternut squash', 'zucchini', 'onion']
self.chicken_tortilla_soup = ['onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH*','
self.creamy_chicken_penne = ['14.5 oz DICED tomatoes', 'penne pasta']
self.salsa_verde_chicken = ['black beans', 'frozen corn', 'salsa verde',]
self.ministrone_soup_w_ground_beef = ['dark red kidney beans', 'spinach CORN TORTILLAS*',]
#self.chicken_tortilla_soup = ['onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVING',]'''
