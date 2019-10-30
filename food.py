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
    #ie 14.5 oz. can  
   
  def __str__(self):
    if not name:
      return amount
    else:
      return amount +  " " + name
    
  def __add__(self, rhs):
    return self.amount + rhs
  
  def __radd__(self, lhs):
    return lhs + self.amount
  
  def __sub__(self, rhs):
    return self.amount - rhs
  
  def __rsub__(self, lhs):
    return lhs - self.amount
  
  def __mul__(self, rhs):
    return self.amount * rhs
  
  def __rmul__(self, lhs):
    return self.amount * lhs
  
  def __truediv__(self, rhs):
    return self.amount / rhs
  
  def __rtruediv__self, lhs):
    return lhs / self.amount
  
  #vary for each food item. All Fractions should round up to total number of items needed. 10 oz, 12 oz would be 2 10 oz, etc?
  def __mod__(self, rhs):
    pass

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

class ShreddedCheddar(Food): #same as above 
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'shredded cheddar'
    self.aisle = 'dairy'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
#Veggies
class baby carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'baby carrots'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'carrots'
    self.aisle = 'veggie'
   
  def __str__(self):
    return Super.__str__() + " " + self.food


class Onion(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'onion'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Spinach(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'spinach'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenBellPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen bell peppers'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenOnions(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'green onions'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DicedTomatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='14.5 oz'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'diced tomatoes'
    self.aisle = 'veggie' #can
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Zucchini(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'zucchini'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SmallCabbage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'small cabbage'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedBellPepper(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red bell pepper'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RainbowPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rainbow peppers'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  #fix below
class ButternutSquash(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butternut squash'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenCorn(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen corn'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DarkRedKidneyBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'dark red kidney beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'grean beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedPotatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red potatoes'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    #play with this one stalks change to bunches or pounds
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CannelliniBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cannellini beans('
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BlackBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'black beans'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
'''
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
 
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
'''

#spices and sauces, pasta
#Non-food items
class FreezerBag(Food):
  def __init__(self, amount=1'):
    Super().__init__(amount)
    self.food = 'freezer bag'
    self.category = 'non-food'
               
  def __str__(self):
    return Super.__str__() + " " + self.food

#modify to meet aisle of store
'''
self.sloppy_joes = ['15 OZ. tomato Sauce']
self.chicken_tikka_masala = ['15 OZ. tomato sauce','15 OZ. tomato sauce']
self.chicken_cordon_bleu_casserole = ['extra wide egg noodles', 'italian bread crumbs']
self.chicken_and_sausage_orzo =['8oz._tomatoe SAUCE', 'orzo']
self.italian_sausage_rigatoni = ['4.5 cups rigatoni']
self.tuscaan_torellini_soup = ['24oz pasta sauce', 'frozen cheese tortellini']
self.white_chicken_chili = ['salsa verde']
self.ranch_popcorn_chicken = ['egg', 'cornflakes',]
self.cheesy_chicken_veggie_casserole = ['ritz', ]
self.jalepeno_and_bacon = ['elbow macoroni' 'jalepeno']
self.indian_butter_chicken = [' '15oz tomatoe sauce', '15oz tomatoe sauce']']
self.chicken_tortilla_soup = ['1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH*','
self.creamy_chicken_penne = ['penne pasta']
self.salsa_verde_chicken = ['salsa verde',]
self.ministrone_soup_w_ground_beef = ['', 'spinach CORN TORTILLAS*',]
#self.chicken_tortilla_soup['1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVIN
'''

#Dry and liquid Measure Equivalents: nested list in food or recipe
'''
Volume (Liquid) 
American Standard      American Standard             Metric
 (Cups & Quarts )           (Ounces)           (Milliliters & Liters)
   2 tbsp                   1 fl. oz.               30 ml
   1/4 cup                  2 fl. oz.               60 ml
   1/2 cup                  4 fl. oz.               125 ml
   1 cup                    8 fl. oz.               250 ml
   1 1/2 cups               12 fl. oz.              375 ml
   2 cups or 1 pint         16 fl. oz.              500 ml
   4 cups or 1 quart        32 fl. oz.              1000 ml or 1 liter
   1 gallon                 128 fl. oz.             4 liters
 
Dry Measure Equivalents
 	 	 	 
 3 teaspoons	 1 tablespoon	 1/2 ounce	 14.3 grams
 2 tablespoons	1/8 cup	 1 ounce	 28.3 grams
 4 tablespoons	 1/4 cup	 2 ounces	 56.7 grams
 5 1/3 tablespoons	 1/3 cup	 2.6 ounces	 75.6 grams
 8 tablespoons	 1/2 cup	 4 ounces	 113.4 grams
 12 tablespoons	 3/4 cup	 6 ounces	 .375 pound
 32 tablespoons	 2 cups	 16 ounces	 1 pound
'''
