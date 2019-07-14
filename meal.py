class Meal:
    def __init__(self, name):
        self.meal_name = name
        self.file_name = "meals/" + self.meal_name + ".txt"
        self.supplies, self.ingredients, self.people  = self.read_file()

    def read_file(self):
        supplies = []
        ingredients = []
        num_people_per_serving = 1 #default
        f= open(self.file_name, "r")
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
                    isSupply = True
                    isIngredient = False
                elif (words[0] == "ingredients"):
                    isSupply = False
                    isIngredient = True
                elif (words[0] == "people"):
                    isPeople = True
                elif isPeople:
                    num_people_per_serving = words[0]
                    isPeople = False
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
        f.close()

        #printed output
        print("MEAL:", self.meal_name)
        print("This feeds", num_people_per_serving, "people")
        if len(supplies) > 0:
            print("\nSUPPLIES")
            for item in supplies:
                print(item[0], item[1])
        if len(ingredients) > 0:
            print("\nINGREDIENTS")
            for item in ingredients:
                print(item[0], item[1])
        print("")

        return supplies, ingredients, num_people_per_serving

    def get_supplies(self):
        return self.supplies

    def get_ingredients(self):
        return self.ingredients

    def get_people(self):
        return self.people
