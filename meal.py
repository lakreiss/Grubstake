class Meal:
    def __init__(self, name):
        self.meal_name = name
        self.file_name = "meals/" + self.meal_name + ".txt"
        self.supplies, self.ingredients, self.per_person_supplies, self.people  = self.read_file()

    def read_file(self):
        supplies = []
        ingredients = []
        per_person_supplies = {}
        num_people_per_serving = 1 #default
        f= open(self.file_name, "r")
        fl = f.readlines()
        is_supply = False
        is_ingredient = False
        is_people = False
        is_per_person_supplies = False
        for line in fl:
            words = line.lower().split()
            if (len(words) == 0):
                continue
            elif (len(words) == 1):
                if (words[0] == "supplies"):
                    is_supply = True
                    is_ingredient = False
                    is_per_person_supplies = False
                elif (words[0] == "ingredients"):
                    is_supply = False
                    is_ingredient = True
                    is_per_person_supplies = False
                elif (words[0] == "per_person_supplies"):
                    is_per_person_supplies = True
                    is_supply = False
                    is_ingredient = False
                elif (words[0] == "people"):
                    is_people = True
                elif is_people:
                    num_people_per_serving = float(words[0])
                    is_people = False
                else:
                    print("ERROR: not enough words")
            else:
                item = words[0]
                number = words[1]
                tuple = (item, number)
                if (is_supply):
                    supplies += [tuple]
                elif (is_ingredient):
                    ingredients += [tuple]
                elif (is_per_person_supplies):
                    per_person_supplies[item] = number
                else:
                    print("ERROR: unclear item type")
        f.close()

        #printed output
        # print("MEAL:", self.meal_name)
        # print("This feeds", num_people_per_serving, "people")
        # if len(supplies) > 0:
        #     print("\nSUPPLIES")
        #     for item in supplies:
        #         print(item[0], item[1])
        # if len(ingredients) > 0:
        #     print("\nINGREDIENTS")
        #     for item in ingredients:
        #         print(item[0], item[1])
        # print("")

        return supplies, ingredients, per_person_supplies, num_people_per_serving

    def get_supplies(self):
        return self.supplies

    def get_ingredients(self):
        return self.ingredients

    def get_people(self):
        return self.people

    def get_per_person_supplies(self):
        return self.per_person_supplies
