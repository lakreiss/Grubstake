class Meal:
    def __init__(self, name):
        self.meal_name = name

    def parse_meal(self):
        supplies = []
        ingredients = []
        file_name = self.meal_name + ".txt"
        f= open(file_name, "r")
        fl = f.readlines()
        isSupply = False
        isIngredient = True
        for line in fl:
            words = line.lower().split()
            if (len(words) == 0):
                print("")
            elif (len(words) == 1):
                if (words[0] == "supplies"):
                    print("SUPPLIES")
                    isSupply = True
                    isIngredient = False
                elif (words[0] == "ingredients"):
                    print("INGREDIENTS")
                    isSupply = False
                    isIngredient = True
                else:
                    print("ERROR: not enough words")
            else:
                item = words[0]
                number = words[1]
                tuple = (item, number)
                if (isSupply):
                    supplies += [tuple]
                elif (isIngredient):
                    ingredients += [tuple]
                else:
                    print("ERROR: unclear item type")
                    
                print(item, number)

        return supplies, ingredients
        f.close()
