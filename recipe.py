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
                        ]

    def __str__(self):
        rep = 'Options are: meats,\nvegtables, suggested_sides, \nchili_spiced_beef_and_carrots, \nmonster_cheese_burgers, \ntuscan_steak_and_green_peppers, \nbeef_and_cabbage_soup, \nsloppy_joes, chicken_spinach_alfredo'
        rep += ', \nchicken_tikka_masala, \nshredded_chicken_fajitas, \nchicken_cordon_bleu_casserole, \nchicken_and_sausage_orzo, \nitalian_sausage_rigatoni, \ngvb_soup_turkey, \ntuscaan_torellini_soup, \nwhite_chicken_chili'
        rep += ', \nranch_popcorn_chicken, \ncheesy_chicken_veggie_casserole, \npulled_pork, \nsuasage_and_peppers, \npotatoe_corn_chowder, \njalepeno_and_bacon, \nindian_butter_chicken, \ncreamy_chicken_penne, \nsalsa_verde_chicken'
        rep += ', \nministrone_soup_w_ground_beef'
        return rep
