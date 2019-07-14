class Meal:
    def __init__(self, name):
        self.meal_name = name

    def parse_meal(self):
        supplies = []
        ingredients = []
        file_name = "meals/" + self.meal_name + ".txt"
        f= open(file_name, "r")
        fl = f.readlines()
        isSupply = False
        isIngredient = False
        isPeople = False
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
                elif (words[0] == "people"):
                    print("PEOPLE")
                    isPeople = True
                elif isPeople:
                    self.people = words[0]
                    isPeople = False
                    print("This feeds", self.people, "people")
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
