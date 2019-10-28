import Food

#create a dictionary of strings to classes
food = {}
food['chicken breast'] = ChickenBreast()
food['ground beef'] = GroundBeef()
food['pork shoulder'] = PorkShoulder()
class Recipe():
    '''Lists of recipes for automate grocery recipes contained in here'''
    def __init__(self):
        self.always_keep_stocked = ['red wine vinegar',
                                    'extra virgin olive oil',
                                    'salt','cumin',
                                    'red pepper flakes',
                                    'paprika',
                                    'garlic powder',
                                    'onion powder',
                                    'crockpot liners',
                                    'peeled garlic,',
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
                                    'chili powder',]


        #1) recipes form new leaf wellness(excluding keep stocked list changed into a list on python
       
        self.meats = ['beef chuck shouulder','ground turkey', 'ham', 'sliced & fat trimmed boneless sirloin tip roast',]
        self.vegtables =['green bell peppers', 'frozen bell peppers', ]
        self.suggested_sides = ['potatoes','rice','broccoli', 'brussel sprouts',]

       
        self.chili_spiced_beef_and_carrots = ["1 Lb beef chuck roast", "1 Lb beef chuck roast", '1 lb baby carrots', '1 lb baby carrots','freezer bag',]
        self.monster_cheese_burgers = ['American cheese']
        self.tuscan_steak_and_green_peppers = ['1 Lb sliced & fat trimmed boneless sirloin tip roast', 'frozen bell peppers','onion', '14.5 oz DICED tomatoes', 'freezer bag',]
        self.beef_and_cabbage_soup = ['small cabage', 'onion', 'carrots', '14.5 oz DICED tomatoes', 'freezer bag',]
        self.sloppy_joes = ['onion','red bell pepper', '15 OZ. tomato Sauce', 'freezer bag',]
        self.chicken_spinach_alfredo = ['heavy cream', 'heavy cream', 'parmesean cheese',  'spinach', 'freezer bag',]
        self.chicken_tikka_masala = ['15 OZ. tomato sauce','15 OZ. tomato sauce','heavy cream', 'freezer bag',]
        self.shredded_chicken_fajitas = ['red bell pepper', 'freezer bag',]
        self.chicken_cordon_bleu_casserole = ['extra wide egg noodles','bone in ham bone steak', 'swiss cheese', 'sour cream', 'italian bread crumbs', 'freezer bag',]
        self.chicken_and_sausage_orzo = ['italian_sausage', '8oz._tomatoe SAUCE', 'orzo','freezer bag',]
        self.italian_sausage_rigatoni = ['ground italian sausage' , '14.5 oz DICED tomatoes','14.5 oz DICED tomatoes', 'onion', '4.5 cups rigatoni', 'freezer bag']
        self.gvb_soup_turkey = ['ground turkey','carrots', 'zucchini',]
        self.tuscaan_torellini_soup = ['24oz pasta sauce', 'cannellini beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini', 'freezer bag',]
        self.white_chicken_chili = ['onion', 'salsa verde', 'cannellini beans', 'cannellini beans', 'freezer_bag',]
        self.ranch_popcorn_chicken = ['egg', 'cornflakes',]
        self.cheesy_chicken_veggie_casserole = ['green onions', 'milk', 'shredded cheddar', 'ritz', 'freezer bag',]
        self.pulled_pork = ['1 Lb pork shoulder','1 Lb pork shoulder' 'onion', 'freezer bag',]
        self.suasage_and_peppers =['1 Lb italian sausage', 'rainbow peppers','rainbow peppers', 'rainbow peppers', 'onion', 'freezer bag',]
        self.potatoe_corn_chowder = ['red potatoes', 'red potatoes', 'red potatoes', 'celery','evaporated milk', 'freezer bag',]
        self.jalepeno_and_bacon = ['elbow macoroni', 'monterey jack cheese,', 'cheddar cheese', 'jalepeno', 'onions', 'bacon', 'freezer bag',]
        self.indian_butter_chicken = ['1 Lb chicken thighs', '1 Lb chicken thighs', 'butter,' '15oz tomatoe sauce', '15oz tomatoe sauce', 'heavy whipping cream', 'heavy whipping cream', 'freezer bag',]
        self.creamy_chicken_penne = ['1 Lb chicken breast', '1 Lb chicken breast', 'parmesan cheese', '14.5 oz DICED tomatoes', 'heavy cream', 'heavy cream', 'penne pasta', 'freezer bag',]
        self.salsa_verde_chicken = [ '1 Lb chicken breast', 'black beans', 'frozen corn', 'cream cheese', 'salsa verde',]
        self.ministrone_soup_w_ground_beef = [ 'dark red kidney beans', 'spinach', 'butternut squash', 'zucchini', 'onion', 'freezer bag',]
        self.chicken_tortilla_soup = ['onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH*','4 CORN TORTILLAS*',]
        #self.chicken_tortilla_soup = ['1 Lb chicken breast', 'onion', 'red bell pepper', '14.5 oz DICED tomatoes', '1.5 cups frozen corn', 'black beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 tea GROUND CUMIN','1/2 tea GARLIC POWDER','4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVING',]
                        ]

    def __str__(self):
        rep = 'Options are: meats,\nvegtables, suggested_sides, \nchili_spiced_beef_and_carrots, \nmonster cheese burgers, \ntuscan steak and green peppers, \nbeef and cabbage soup, \nsloppy joes, chicken spinach alfredo'
        rep += ', \nchicken tikka masala, \nshredded chicken fajitas, \nchicken cordon bleu casserole, \nchicken and sausage orzo, \nitalian sausage rigatoni, \ngvb soup turkey, \ntuscaan torellini soup, \nwhite chicken chili'
        rep += ', \nranch popcorn chicken, \ncheesy chicken veggie casserole, \npulled pork, \nsuasage and peppers, \npotatoe corn chowder, \njalepeno and bacon, \nindian butter chicken, \ncreamy chicken penne, \nsalsa verde chicken'
        rep += ', \nministrone soup w ground_beef\nchicken tortilla soup'
        return rep

    
    '''
     self.meats = ['ground_beef','beef chuck shouulder', '1_Lb__chicken_breast','ground_turkey', 'ham', 'sliced _&_fat_trimmed_boneless_sirloin_tip_roast',]
        self.vegtables =['green bell peppers', 'frozen_bell_peppers', ]
        self.suggested_sides = ['potatoes','rice','broccoli', 'brussel sprouts',]

       
        self.chili_spiced_beef_and_carrots = ["1_Lb_beef_chuck_roast", "1_Lb_beef_chuck_roast", '1_lb_baby_carrots', '1_lb_baby_carrots','freezer_bag',]
        self.monster_cheese_burgers = ['1_Lb_ground_beef','1_Lb_ground_beef' , 'American_cheese']
        self.tuscan_steak_and_green_peppers = ['1_Lb_sliced _&_fat_trimmed_boneless_sirloin_tip_roast', 'frozen_bell_peppers','onion', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
        self.beef_and_cabbage_soup = ['1_Lb_ground_beef', 'small cabage', 'onion', 'carrots', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
        self.sloppy_joes = ['1_Lb_ground_beef','onion','red_bell_pepper', '15_OZ. tomato_SAUCE', 'freezer_bag',]
        self.chicken_spinach_alfredo = ['1_Lb_1_Lb__chicken_breast', 'heavy_cream', 'heavy_cream', 'parmesean_cheese',  'spinach', 'freezer_bag',]
        self.chicken_tikka_masala = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', '15_OZ. tomato_SAUCE','15_OZ. tomato_SAUCE','heavy_cream', 'freezer_bag',]
        self.shredded_chicken_fajitas = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', 'red_bell_pepper', 'freezer_bag',]
        self.chicken_cordon_bleu_casserole = ['extra_wide_egg_noodles', '1_Lb__chicken_breast', '1_Lb__chicken_breast','bone_in_ham_bone_steak', 'swiss_cheese', 'sour_cream', 'italian_bread_crumbs', 'freezer_bag',]
        self.chicken_and_sausage_orzo = ['italian_sausage', '1_Lb__chicken_breast', '8oz._tomatoe_SAUCE', 'orzo','freezer_bag', ]
        self.italian_sausage_rigatoni = ['ground_italian_sausage' , '14.5_oz_DICED_tomatoes','14.5_oz_DICED_tomatoes', 'onion', '4.5_cups_rigatoni', 'freezer_bag']
        self.gvb_soup_turkey = ['ground_turkey','carrots', 'zucchini',]
        self.tuscaan_torellini_soup = ['24oz_pasta_sauce', 'cannellini_beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini', 'freezer_bag',]
        self.white_chicken_chili = ['1_Lb__chicken_breast', 'onion', 'salsa verde', 'cannellini_beans', 'cannellini_beans', 'freezer_bag', ]
        self.ranch_popcorn_chicken = [ 'egg','1_Lb__chicken_breast', '1_Lb__chicken_breast', 'cornflakes' ]
        self.cheesy_chicken_veggie_casserole = ['1_Lb__chicken_breast', '1_Lb__chicken_breast','green_onions', 'milk', 'shredded_cheddar', 'ritz', 'freezer_bag', ]
        self.pulled_pork = ['1_Lb_pork shoulder','1_Lb_pork_shoulder' 'onion', 'freezer_bag', ]
        self.suasage_and_peppers =[ '1_Lb_italian_sausage', 'rainbow_peppers','rainbow_peppers', 'rainbow_peppers', 'onion', 'freezer_bag',  ]
        self.potatoe_corn_chowder = ['red_potatoes', 'red_potatoes', 'red_potatoes', 'celery','evaporated_milk', 'freezer_bag', ]
        self.jalepeno_and_bacon = ['elbow_macoroni', 'monterey_jack_cheese,', 'cheddar_cheese', 'jalepeno', 'onions', 'bacon', 'freezer_bag', ]
        self.indian_butter_chicken = ['1_Lb_chicken_thighs', '1_Lb_chicken_thighs', 'butter,' '15oz_tomatoes_SAUCE', '15oz_tomatoes_SAUCE', 'heavy_whipping_cream', 'heavy_whipping_cream', 'freezer_bag', ]
        self.creamy_chicken_penne = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'parmesan cheese', '14.5_oz_DICED_tomatoes', 'heavy_cream', 'heavy_cream', 'penne pasta', 'freezer_bag',]
        self.salsa_verde_chicken = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'black_beans', 'frozen_corn', 'cream_cheese', 'salsa_verde', ]
        self.ministrone_soup_w_ground_beef = ['1_Lb_ground_beef', 'dark_red_kidney_beans', 'spinach', 'butternut_squash', 'zucchini', 'onion', 'freezer_bag', ]
        self.chicken_tortilla_soup = chicken_tortilla_soup = [ '1_Lb__chicken_breast', 'onion', 'red_bell_pepper', '14.5_oz_DICED_tomatoes', '1.5 cups frozen corn', 'black_beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 TEASPOON GROUND CUMIN','1/2 TEASPOON GARLIC POWDER', '4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVING',
'''
