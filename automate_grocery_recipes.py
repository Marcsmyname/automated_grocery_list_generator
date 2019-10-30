from recipe import Recipe
import Food

def cleanPrint(aList, Dict=False):
    """Prints inside of a list or dictionary. List is the Default print."""
    count = len(aList)
    counterDict = {}
    
    if Dict:    
        for item in aList:
            if item not in counterDict.keys():
                counterDict[item] = 1
            else:
                counterDict[item] = counterDict[item] + 1

        count = len(counterDict)
        for key, value in counterDict.items():
            if count == 1:
                print(key + ": " + str(value))
            else:
                print(key + ": " + str(value) + ",")
                count = count - 1
    else:
        for item in aList:
            if count == 1:
                print(item)
            else:
                print(item + ",")
                count = count - 1
                
    return counterDict

def parse(name, foodDict):
    foodList = [None] * 2 
    rhs = ''
    inc = 1
    lhs = name[inc]

    while lhs not in foodDict:
        inc = inc + 1
        lhs = name[:inc]
        rhs = name[inc:]

    rhs foodList[1]

    name = lhs
    rhs = ''
    inc = 0
    lhs = name[inc]
    while name[inc].isDigit() or name[0] == '/':
        inc = inc + 1
        lhs = name[:inc]
        rhs = name[inc:]
    foodList[0] = (lhs, rhs)

    return foodList

recipes = Recipe()
border = "="*11
counterDict = {}
new_item = ''
Grocerys = {}
shopping_list = []
food_list = []
store_list = []

#these are the store aisles that will be used to eventually sort grocery list
aisles = [['produce'],['meat', 'cheese', 'lunch meat',], ['dairy', 'eggs', 'juice', 'pies', 'yogurt', 'butter'],
          ['frozen vegetables'], ['housewares'], ['cereal', 'coffee/tea'], ['baking', 'spices', 'PBJ'],
          ['boxed dinner', 'canned meat', 'pasta/sauce'], ['soup', 'mexican', 'asian'], 
          ['condiments', 'canned fruits/veggies & juice'], ['cookies & crackers'], ['candy, snacks, & chips'], ['bread'],
         ['ice']]

while new_item.upper() != "DONE":
    print("What should we buy from the store?  \n")
    print("Enter 'DONE' to stop adding items. \n'HELP' to see items.")
    print(border + "Remember: Recipes must be entered as a list in the program first"
          + border)
    
    #asks for new items
    new_item = input("Enter a Recipe ")
    
    if new_item == 'monster cheese burgers':
        shopping_list.extend(recipes.monster_cheese_burgers)
    elif new_item == 'chili spiced beef and carrots':
        shopping_list.extend(recipes.chili_spiced_beef_and_carrots)
    elif new_item == 'tuscan steak and green peppers':
        shopping_list.extend(recipes.tuscan_steak_and_green_peppers)
    elif new_item == 'beef and cabbage soup':
        shopping_list.extend(recipes.beef_and_cabbage_soup)
    elif new_item == 'sloppy joes':
        shopping_list.extend(recipes.sloppy_joes)
    elif new_item == 'chicken spinach alfredo':
        shopping_list.extend(recipes.chicken_spinach_alfredo)
    elif new_item == 'chicken tikka masala':
        shopping_list.extend(recipes.chicken_tikka_masala)
    elif new_item == 'shredded chicken fajitas':
        shopping_list.extend(recipes.shredded_chicken_fajitas)
    elif new_item == 'chicken cordon bleu casserole':
        shopping_list.extend(recipes.chicken_cordon_bleu_casserole)
    elif new_item == 'chicken and sausage orzo':
        shopping_list.extend(recipes.chicken_and_sausage_orzo)
    elif new_item == 'italian sausage rigatoni':
        shopping_list.extend(recipes.italian_sausage_rigatoni)
    elif new_item == 'gvb soup turkey':
        shopping_list.extend(recipes.gvb_soup_turkey)
    elif new_item == 'tuscaan torellini soup':
        shopping_list.extend(recipes.tuscaan_torellini_soup)
    elif new_item == 'white chicken chili':
        shopping_list.extend(recipes.white_chicken_chili)
    elif new_item == 'ranch popcorn chicken':
        shopping_list.extend(recipes.ranch_popcorn_chicken)
    elif new_item == 'cheesy chicken veggie casserole':
        shopping_list.extend(recipes.cheesy_chicken_veggie_casserole)
    elif new_item == 'pulled pork':
        shopping_list.extend(recipes.pulled_pork)
    elif new_item == 'suasage and peppers':
        shopping_list.extend(recipes.suasage_and_peppers)
    elif new_item == 'potatoe corn chowder':
        shopping_list.extend(recipes.potatoe_corn_chowder)
    elif new_item == 'jalepeno and bacon':
        shopping_list.extend(recipes.jalepeno_and_bacon)
    elif new_item == 'indian butter chicken':
        shopping_list.extend(recipes.indian_butter_chicken)
    elif new_item == 'salsa verde chicken':
        shopping_list.extend(recipes.salsa_verde_chicken)
    elif new_item == 'chicken tortilla soup':
        shopping_list.extend(recipes.chicken_tortilla_soup)
    elif new_item.upper() == "HELP":
        print(recipes)
    elif new_item.upper() != "DONE":
        print("Your item is invalid, try again. Type HELP to see all items.")
        
for item in shopping_list:
    print(item)

counter = cleanPrint(shopping_list, True)
print("\nAlso Stock your Pantry with these items:\n")
cleanPrint(recipes.always_keep_stocked)

#Count all of the ingredients after adding them up.
total = 0
for recipe in counter.keys():
    total = total + counter[recipe]
    print( recipe + " " + str(counter[recipe]))
print('* items are not needed until day of cooking.')

print("There are " + str(total) + " ingredients to buy. Not including pantry items.")
#print("There are " + str(len(counter.keys())) + " ingredients to buy. Not including pantry items.")
