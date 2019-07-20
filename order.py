from meal import Meal
import sys, math, os

class Order:
    cur_session = 3
    overnight_day = 2
    order_info = {} #contains counselor, unit, item_list, num_people, session, pickup_day, pickup_time, dropoff_day, dropoff_time

    def __init__(self, unit, counselor, item_list, num_people, session=cur_session, pickup_day=overnight_day, pickup_time="2:30", dropoff_day=(overnight_day+1), dropoff_time="11:00", needs_options=False):
        self.order_info["unit"] = unit
        self.order_info["counselor"] = counselor
        self.order_info["item_list"] = item_list
        self.order_info["num_people"] = int(num_people)
        self.order_info["session"] = session
        self.order_info["pickup_day"] = pickup_day
        self.order_info["pickup_time"] = pickup_time
        self.order_info["drop_off_day"] = dropoff_day
        self.order_info["drop_off_time"] = dropoff_time
        self.order_info["needs_options"] = needs_options
        self.log_order()

    #only used for debugging
    def get_order_needs(self):
        for item in self.order_info["item_list"]:
            meal = Meal(item)
            meal_supplies = meal.get_supplies()
            meal_ingredients = meal.get_ingredients()
            meal_people = meal.get_people()
            meal_per_person_supplies = meal.get_per_person_supplies()
        return 'get_order_needs complete'

    def log_order(self):
        #THIS SECTION IS FOR THE ENTIRE DAY'S LOG -- ALL CABINS CONTRIBUTE TO THIS LOG
        #makes a folder if folder doesn't already exist
        session_log_file = "orders/session_" + str(self.order_info["session"])
        if not os.path.exists(session_log_file):
            os.makedirs(session_log_file)
        #makes the file name
        day_log_file = session_log_file + "/day_" + str(self.order_info["pickup_day"]) + ".txt"
        day_file = open(day_log_file, "a")

        self.log_day_file(day_file)

        #THIS SECTION IS ONLY FOR ONE CABIN'S LOG -- EACH CABIN HAS THEIR OWN FILE
        #makes a folder if folder doesn't already exist
        cabin_log_folder = session_log_file + "/day_" + str(self.order_info["pickup_day"])
        if not os.path.exists(cabin_log_folder):
            os.makedirs(cabin_log_folder)
        cabin_log_file = cabin_log_folder + "/" + str(self.order_info["counselor"]) + ".txt"
        cabin_file = open(cabin_log_file, "w")

        self.log_cabin_file(cabin_file)

    def log_day_file(self, day_file):
        #sort keys to standardize output
        all_keys = self.dictionary_to_sorted_list(self.order_info)

        #collect all order info
        text = ""
        for key in all_keys:
            if (text == ""):
                text += key + " " + str(self.order_info[key])
            else:
                text += ", " + key + " " + str(self.order_info[key])
        text += "\n"
        day_file.write(text)

    def log_cabin_file(self, cabin_file):
        #sort keys to standardize output
        all_keys = []
        for key in self.order_info:
            all_keys += [key]
        all_keys.sort()

        #collect all order info
        text = ""
        for key in all_keys:
            text += key + " " + str(self.order_info[key]).upper() + "\n"
        cabin_file.write(text)
        cabin_file.write("\n")

        #collect all meals
        all_meals = []
        for item in self.order_info["item_list"]:
            meal = Meal(item)
            all_meals += [meal]

        #calculate all supplies and ingredients
        all_supplies = {}
        all_ingredients = {}
        all_pp = {}
        for meal in all_meals:
            meal_supplies = meal.get_supplies()
            meal_ingredients = meal.get_ingredients()
            meal_pp = meal.get_per_person_supplies()
            meal_people = meal.get_people()
            # print(meal.meal)
            # print(meal_supplies)
            # print(meal_ingredients)
            # print(meal_people)

            #adds supplies if supply hasn't been added yet
            for supply in meal_supplies:
                if supply[0] not in all_supplies:
                    all_supplies[supply[0]] = int(supply[1])
                else:
                    old_supply_num = all_supplies[supply[0]]
                    new_supply_num = int(supply[1])
                    if (old_supply_num < new_supply_num):
                        all_supplies[supply[0]] = new_supply_num

            # print("ingred list 1", all_ingredients)
            #adds ingredient
            for ingredient in meal_ingredients:
                num_to_add = math.ceil(float(ingredient[1]) * (self.order_info["num_people"] / meal_people))
                if ingredient[0] in all_ingredients:
                    all_ingredients[ingredient[0]] = all_ingredients[ingredient[0]] + num_to_add
                else:
                    all_ingredients[ingredient[0]] = num_to_add

            # print("ingred list 2", all_ingredients)

            for per_person in meal_pp:
                num_to_add = (int(per_person[1]) * self.order_info["num_people"])
                if per_person[0] not in all_pp:
                    all_pp[per_person[0]] = num_to_add
                else:
                    old_pp_num = all_pp[per_person[0]]
                    new_pp_num = int(per_person[1])
                    if (old_pp_num < new_pp_num):
                        all_pp[per_person[0]] = new_pp_num

        #sort lists so that each output is deterministic
        supplies_list = self.dictionary_to_sorted_list(all_supplies)
        ingredients_list = self.dictionary_to_sorted_list(all_ingredients)
        pp_list = self.dictionary_to_sorted_list(all_pp)

        #prints to file, overwriting anything that was written before
        cabin_file.write("SUPPLIES\n")
        for supply in supplies_list:
            cabin_file.write(supply + " " + str(all_supplies[supply]) + "\n")
        cabin_file.write("\n")
        for per_person in pp_list:
            cabin_file.write(per_person + " " + str(all_pp[per_person]) + "\n")
        cabin_file.write("\n")
        cabin_file.write("INGREDIENTS\n")
        for ingredient in ingredients_list:
            cabin_file.write(ingredient + " " + str(all_ingredients[ingredient]) + "\n")

    def dictionary_to_sorted_list(self, dict):
        all_keys = []
        for key in dict:
            all_keys += [key]
        all_keys.sort()
        return all_keys
