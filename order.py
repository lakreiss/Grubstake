from meal import Meal

class Order:
    def __init__(self, item_list_in, num_people_in):
        self.item_name_list = item_list_in
        self.num_people = num_people_in

    def output_order_needs(self):
        for item_name in self.item_name_list:
            meal = Meal(item_name)
            meal_supplies, meal_ingredients = meal.parse_meal()
        print(self.num_people)
        return 'output_order_needs complete'
