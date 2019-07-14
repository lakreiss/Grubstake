from meal import Meal

class Order:
    cur_session = 3
    overnight_day = 2
    order_info = {} #contains counselor_name, unit_name, item_name_list, num_people, session, pickup_day, pickup_time, dropoff_day, dropoff_time

    def __init__(self, counselor_name, unit_name, item_list, num_people, session=cur_session, pickup_day=overnight_day, pickup_time=1430, dropoff_day=(overnight_day+1), dropoff_time=1100):
        self.order_info["counselor_name"] = counselor_name
        self.order_info["unit_name"] = unit_name
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
            meal_supplies, meal_ingredients = meal.parse_meal()
        return 'output_order_needs complete'

    def log_order(self):
        session_log_file_name = "sessions/" + str(self.order_info["session"]) + ".txt"
        f = open(session_log_file_name, "a")
        text = ""
        for key in self.order_info:
            text += key + " " + str(self.order_info[key]) + "\n"
        print(text)
