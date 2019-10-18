from pprint import pprint 
from collections import Counter



always_keep_stocked = ['red wine vinegar',
                       'extra virgin olive oil',
                       'salt','cumin',
                       'red pepper flakes',
                       'paprika',
                       'garlic powder',
                       'onion powder',
                       'crockpot liners',
                       'peeled garlic,'
                       'mayonaise',
                       'montreal steak seasoning',
                       'italian seasoning',
                       'pepper',
                       'bay leaves',
                       'beef broth',
                       'brown sugar',
                       'worchestershire sauce',
                       'parsley',
                       'honey',
                       'lemons/lemon juice',
                       'dijon mustard',
                       'butter',
                       'dill',
                       'apple cider vinegar',
                       'chili powder',
                       ]


#1) recipes form new leaf wellness(excluding keep stocked list changed into a list on python

meats = ['ground_beef','beef chuck shouulder', '1_Lb__chicken_breast','ground_turkey', 'ham', 'sliced _&_fat_trimmed_boneless_sirloin_tip_roast',]
vegtables =['green bell peppers', 'frozen_bell_peppers', ]
suggested_sides = ['potatoes','rice','broccoli', 'brussel sprouts',]
#recipes, each iteration of meat is equal to one pound. each onion is one cup red_bell_peppers medium heavy_cream = 1 cup parmesean_cheese' = 1 cup
# spinach = 5 oz swiss_cheese = 8 oz, sour_cream = 8 ounce orzo =1 cup, #zucchini = 3 or 4 small salsa verde = 16oz.
# cornflakes only 8 oz. ritz = 2 sleeves
#measurements italian_sausage = 8



chili_spiced_beef_and_carrots = ["1_Lb_beef_chuck_roast", "1_Lb_beef_chuck_roast", '1_lb_baby_carrots', '1_lb_baby_carrots','freezer_bag',]
monster_cheese_burgers = ['1_Lb_ground_beef','1_Lb_ground_beef' , 'American_cheese']
tuscan_steak_and_green_peppers = ['1_Lb_sliced _&_fat_trimmed_boneless_sirloin_tip_roast', 'frozen_bell_peppers','onion', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
beef_and_cabbage_soup = ['1_Lb_ground_beef', 'small cabage', 'onion', 'carrots', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
sloppy_joes = ['1_Lb_ground_beef','onion','red_bell_pepper', '15_OZ. tomato_SAUCE', 'freezer_bag',]
chicken_spinach_alfredo = ['1_Lb_1_Lb__chicken_breast', 'heavy_cream', 'heavy_cream', 'parmesean_cheese',  'spinach', 'freezer_bag',]
chicken_tikka_masala = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', '15_OZ. tomato_SAUCE','15_OZ. tomato_SAUCE','heavy_cream', 'freezer_bag',]
shredded_chicken_fajitas = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', 'red_bell_pepper', 'freezer_bag',]
chicken_cordon_bleu_casserole = ['extra_wide_egg_noodles', '1_Lb__chicken_breast', '1_Lb__chicken_breast','bone_in_ham_bone_steak', 'swiss_cheese', 'sour_cream', 'italian_bread_crumbs', 'freezer_bag',]
chicken_and_sausage_orzo = ['italian_sausage', '1_Lb__chicken_breast', '8oz._tomatoe_SAUCE', 'orzo','freezer_bag', ]
italian_sausage_rigatoni = ['ground_italian_sausage' , '14.5_oz_DICED_tomatoes','14.5_oz_DICED_tomatoes', 'onion', '4.5_cups_rigatoni', 'freezer_bag']
gvb_soup_turkey = ['ground_turkey','carrots', 'zucchini',]
tuscaan_torellini_soup = ['24oz_pasta_sauce', 'cannellini_beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini', 'freezer_bag',]
white_chicken_chili = ['1_Lb__chicken_breast', 'onion', 'salsa verde', 'cannellini_beans', 'cannellini_beans', 'freezer_bag', ]
ranch_popcorn_chicken = [ 'egg','1_Lb__chicken_breast', '1_Lb__chicken_breast', 'cornflakes' ]
cheesy_chicken_veggie_casserole = ['1_Lb__chicken_breast', '1_Lb__chicken_breast','green_onions', 'milk', 'shredded_cheddar', 'ritz', 'freezer_bag', ]
pulled_pork = ['1_Lb_pork shoulder','1_Lb_pork_shoulder' 'onion', 'freezer_bag', ]
suasage_and_peppers =[ '1_Lb_italian_sausage', 'rainbow_peppers','rainbow_peppers', 'rainbow_peppers', 'onion', 'freezer_bag',  ]
potatoe_corn_chowder = ['red_potatoes', 'red_potatoes', 'red_potatoes', 'celery','evaporated_milk', 'freezer_bag', ]
jalepeno_and_bacon = ['elbow_macoroni', 'monterey_jack_cheese,', 'cheddar_cheese', 'jalepeno', 'onions', 'bacon', 'freezer_bag', ]
indian_butter_chicken = ['1_Lb_chicken_thighs', '1_Lb_chicken_thighs', 'butter,' '15oz_tomatoes_SAUCE', '15oz_tomatoes_SAUCE', 'heavy_whipping_cream', 'heavy_whipping_cream', 'freezer_bag', ]
creamy_chicken_penne = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'parmesan cheese', '14.5_oz_DICED_tomatoes', 'heavy_cream', 'heavy_cream', 'penne pasta', 'freezer_bag',]
salsa_verde_chicken = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'black_beans', 'frozen_corn', 'cream_cheese', 'salsa_verde', ]
ministrone_soup_w_ground_beef = ['1_Lb_ground_beef', 'dark_red_kidney_beans', 'spinach', 'butternut_squash', 'zucchini', 'onion', 'freezer_bag', ]



            


                        

#Treehouse code to start with:

shopping_list = []

while True:
    print("What should we buy from the store?  \n")
    print("""Enter 'DONE' to stop adding items. \n
===========Remember: Recipes must be entered as a list in the program first===========
          """)


    #asks for new items
    new_item = input("Enter a Recipe ")

    #be able to quit the app
    if new_item == 'monster_cheese_burgers':
        shopping_list.extend(monster_cheese_burgers)
    elif new_item == 'chili_spiced_beef_and_carrots':
        shopping_list.extend(chili_spiced_beef_and_carrots)
    elif new_item == 'tuscan_steak_and_green_peppers':
        shopping_list.extend(tuscan_steak_and_green_peppers)
    elif new_item == 'beef_and_cabbage_soup':
        shopping_list.extend(beef_and_cabbage_soup)
    elif new_item == 'sloppy_joes':
        shopping_list.extend(sloppy_joes)
    elif new_item == 'chicken_spinach_alfredo':
        shopping_list.extend(chicken_spinach_alfredo)
    elif new_item == 'monster_cheese_burgers':
        shopping_list.extend(chicken_tikka_masala)
    elif new_item == 'shredded_chicken_fajitas':
        shopping_list.extend(shredded_chicken_fajitas)
    elif new_item == 'chicken_cordon_bleu_casserole':
        shopping_list.extend(chicken_cordon_bleu_casserole)
    elif new_item == 'chicken_and_sausage_orzo':
        shopping_list.extend(chicken_and_sausage_orzo)
    elif new_item == 'italian_sausage_rigatoni':
        shopping_list.extend(italian_sausage_rigatoni)
    elif new_item == 'gvb_soup_turkey':
        shopping_list.extend(gvb_soup_turkey)
    elif new_item == 'tuscaan_torellini_soup':
        shopping_list.extend(tuscaan_torellini_soup)
    elif new_item == 'white_chicken_chili':
        shopping_list.extend(white_chicken_chili)
    elif new_item == 'ranch_popcorn_chicken':
        shopping_list.extend(ranch_popcorn_chicken)
    elif new_item == 'cheesy_chicken_veggie_casserole':
        shopping_list.extend(cheesy_chicken_veggie_casserole)
    elif new_item == 'pulled_pork':
        shopping_list.extend(pulled_pork)
    elif new_item == 'suasage_and_peppers':
        shopping_list.extend(suasage_and_peppers)
    elif new_item == 'potatoe_corn_chowder':
        shopping_list.extend(potatoe_corn_chowder)
    elif new_item == 'jalepeno_and_bacon':
        shopping_list.extend(jalepeno_and_bacon)
    elif new_item == 'indian_butter_chicken':
        shopping_list.extend(indian_butter_chicken)
    elif new_item == 'salsa_verde_chicken':
        shopping_list.extend(salsa_verde_chicken)
    elif new_item == 'salsa_verde_chicken':
        shopping_list.extend(salsa_verde_chicken)
    elif new_item == 'DONE':
        break
        for item in shopping_list:
            print(item)


#Counter program to add the number of items to the list
    
counts = Counter(shopping_list)
pprint(counts)

print("\nAlso Stock your Pantry with these items:\n")
pprint(always_keep_stocked)
#Count all of the ingredients after adding them up.
