from meal import Meal
import os

class Order:
    cur_session = 3
    overnight_day = 2
    order_info = {} #contains counselor_name, unit_name, item_name_list, num_people, session, pickup_day, pickup_time, dropoff_day, dropoff_time

    def __init__(self, unit_name, counselor_name, item_list, num_people, session=cur_session, pickup_day=overnight_day, pickup_time=1430, dropoff_day=(overnight_day+1), dropoff_time=1100):
        self.order_info["unit_name"] = unit_name
        self.order_info["counselor_name"] = counselor_name
        self.order_info["item_name_list"] = item_list
        self.order_info["num_people"] = num_people
        self.order_info["session"] = session
        self.order_info["pickup_day"] = pickup_day
        self.order_info["pickup_time"] = pickup_time
        self.order_info["dropoff_day"] = dropoff_day
        self.order_info["dropoff_time"] = dropoff_time
        self.log_order()

    def output_order_needs(self):
        for item_name in self.order_info["item_name_list"]:
            meal = Meal(item_name)
            meal_supplies = meal.get_supplies()
            meal_ingredients = meal.get_ingredients()
            meal_people = meal.get_people()
        return 'output_order_needs complete'

    def log_order(self):

        #THIS SECTION IS FOR THE ENTIRE DAY'S LOG -- ALL CABINS CONTRIBUTE TO THIS LOG
        #makes a folder if folder doesn't already exist
        session_log_file_name = "sessions/session_" + str(self.order_info["session"])
        if not os.path.exists(session_log_file_name):
            os.makedirs(session_log_file_name)
        #makes the file name
        day_log_file_name = session_log_file_name + "/day_" + str(self.order_info["pickup_day"]) + ".txt"
        day_file = open(day_log_file_name, "a")

        self.log_day_file(day_file)

        #THIS SECTION IS ONLY FOR ONE CABIN'S LOG -- EACH CABIN HAS THEIR OWN FILE
        #makes a folder if folder doesn't already exist
        cabin_log_folder_name = session_log_file_name + /day_" + str(self.order_info["pickup_day"])
        if not os.path.exists(cabin_log_folder_name):
            os.makedirs(cabin_log_folder_name)
        cabin_log_file_name = cabin_log_folder_name + "/" + str(self.order_info["counselor_name"]) + ".txt"
        cabin_file = open(cabin_log_file_name, "a")

        self.log_cabin_file(cabin_file)

    def log_day_file(self, day_file)
        #sort keys to standardize output
        all_keys = []
        for key in self.order_info:
            all_keys += [key]
        all_keys.sort()

        #collect all order info
        text = ""
        for key in all_keys:
            if (text == ""):
                text += key + " " + str(self.order_info[key])
            else:
                text += ", " + key + " " + str(self.order_info[key])
        text += "\n"
        day_file.write(text)

    def log_cabin_file(self, cabin_file) #TODO
        #sort keys to standardize output
        all_keys = []
        for key in self.order_info:
            all_keys += [key]
        all_keys.sort()

        #collect all order info
        text = ""
        for key in all_keys:
            if (text == ""):
                text += key + " " + str(self.order_info[key])
            else:
                text += ", " + key + " " + str(self.order_info[key])
        text += "\n"
        cabin_file.write(text)
