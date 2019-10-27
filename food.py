from mixed import Mixed
#from decimal import Decimal

class Food():
  """Base class for all food in shopping list."""
  #unit for single unit of food
  self.names = ('tsp', 'tbsp', 'cup', 'oz', 'can', ) #increase for all units of measurment
  
  def __init__(self, amount=0, name=''):
    self.amount = Mixed(amount)
    self.name = name;
    #14.5 oz. can  
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
  def __str__(self):
    return Super.__str__() + " " + self.food

class BeefChuckRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'beef chuck roast'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundBeef(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground beef'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground italian sausage'
  def __str__(self):
    return Super.__str__() + " " + self.food

class ItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'italian sausage'
  def __str__(self):
    return Super.__str__() + " " + self.food

class PorkShoulder(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'pork shoulder'
  def __str__(self):
    return Super.__str__() + " " + self.food

class Bacon(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bacon'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundTurkey(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground turkey'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class HamSteak(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bone in ham bone steak'
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenThighs(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'chicken thighs'
  def __str__(self):
    return Super.__str__() + " " + self.food

class SerloinTipRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'sliced & fat trimmed boneless sirloin tip roast'
  def __str__(self):
    return Super.__str__() + " " + self.food

  #Dairy

class AmericanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HeavyCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class Milk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
  def __str__(self):
    return Super.__str__() + " " + self.food

class HeavyWhippingCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
  def __str__(self):
    return Super.__str__() + " " + self.food

#Non-food items
class FreezerBag(Food):
  def __init__(self, amount=1'):
    Super().__init__(amount)
    self.food = 'freezer bag'
  def __str__(self):
    return Super.__str__() + " " + self.food

'''  self.chili_spiced_beef_and_carrots = ['1 lb baby carrots', '1 lb baby carrots','',]
self.tuscan_steak_and_green_peppers = [ 'frozen bell peppers','onion', '14.5 oz DICED tomatoes']
self.beef_and_cabbage_soup = ['small cabage', 'onion', 'carrots', '14.5 oz DICED tomatoes']
self.sloppy_joes = ['onion','red bell pepper', '15 OZ. tomato Sauce']
self.chicken_spinach_alfredo = ['parmesean cheese',  'spinach']
self.chicken_tikka_masala = ['15 OZ. tomato sauce','15 OZ. tomato sauce']
self.shredded_chicken_fajitas = ['red bell pepper']
self.chicken_cordon_bleu_casserole = ['extra wide egg noodles', 'swiss cheese', 'sour cream', 'italian bread crumbs']
self.chicken_and_sausage_orzo =['8oz._tomatoe SAUCE', 'orzo']
self.italian_sausage_rigatoni = ['14.5 oz DICED tomatoes','14.5 oz DICED tomatoes', 'onion', '4.5 cups rigatoni']
self.gvb_soup_turkey = ['carrots', 'zucchini',]
self.tuscaan_torellini_soup = ['24oz pasta sauce', 'cannellini beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini']
self.white_chicken_chili = ['salsa verde', 'cannellini beans', 'cannellini beans', ]
self.ranch_popcorn_chicken = ['egg', 'cornflakes',]
self.cheesy_chicken_veggie_casserole = ['green onions', 'milk', 'shredded cheddar', 'ritz', ]
self.pulled_pork = ['onion',]
self.suasage_and_peppers =['rainbow peppers','rainbow peppers', 'rainbow peppers', 'onion']
self.potatoe_corn_chowder = ['red potatoes', 'red potatoes', 'red potatoes', 'celery','evaporated milk']
self.jalepeno_and_bacon = ['elbow macoroni', 'monterey jack cheese,', 'cheddar cheese', 'jalepeno', 'onions']
self.indian_butter_chicken = ['butter,' '15oz tomatoe sauce', '15oz tomatoe sauce']
self.creamy_chicken_penne = ['parmesan cheese', '14.5 oz DICED tomatoes', 'penne pasta']
self.salsa_verde_chicken = ['black beans', 'frozen corn', 'cream cheese', 'salsa verde',]
self.ministrone_soup_w_ground_beef = ['dark red kidney beans', 'spinach', 'butternut squash', 'zucchini', 'onion']
self.chicken_tortilla_soup = ['onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH*','4 CORN TORTILLAS*',]
#self.chicken_tortilla_soup = ['onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVING',]'''
