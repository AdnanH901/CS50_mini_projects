def main():
    nutrition_table = [ { "fruits" : "Apple"          , "calories" : 130 },
                        { "fruits" : "Avocado"        , "calories" :  50 },
                        { "fruits" : "Banana"         , "calories" : 110 },
                        { "fruits" : "Cantaloupe"     , "calories" :  50 },
                        { "fruits" : "Grapefruit"     , "calories" :  60 },
                        { "fruits" : "Grapes"         , "calories" :  90 },
                        { "fruits" : "Honeydew Melon" , "calories" :  50 },
                        { "fruits" : "Kiwifruit"      , "calories" :  90 },
                        { "fruits" : "Lemon"          , "calories" :  15 },
                        { "fruits" : "Lime"           , "calories" :  20 },
                        { "fruits" : "Nectarine"      , "calories" :  60 },
                        { "fruits" : "Orange"         , "calories" :  80 },
                        { "fruits" : "Peach"          , "calories" :  60 },
                        { "fruits" : "Pear"           , "calories" : 100 },
                        { "fruits" : "Pineapple"      , "calories" :  50 },
                        { "fruits" : "Plums"          , "calories" :  70 },
                        { "fruits" : "Strawberries"   , "calories" :  50 },
                        { "fruits" : "Sweet Cherries" , "calories" : 100 },
                        { "fruits" : "Tangerine"      , "calories" :  50 },
                        { "fruits" : "Watermelon"     , "calories" :  80 } ]
    fruit = input("Fruit: ").title()
    for nutrition in nutrition_table:
        if fruit == nutrition["fruits"]:
            print(nutrition["calories"])
main()