#! /usr/bin/env python
import sys
import gui
from order import Order

def main():
    #
    # Do something ... Whatever processing you need to do, make it happen here.
    # Don't shove everything into main, break it up into testable functions!
    #
    # Whatever this function returns, is what the exit code of the interpreter,
    # i.e. your script, will be.  Because main is called by sys.exit(), it will
    # behave differently depending on what you return.
    #
    # So, if you return None, 0 is returned.  If you return integer, that
    # return code is used.  Anything else is printed to the console and 1 (error)
    # is returned.

    main = gui.GUI()

    # make_orders()

    #if an_error_occurred:
    #    return 'I\'m returning a string, it will be printed and 1 returned'
    #

    # Otherwise 0, success is returned.
    return 0


#USED FOR TESTING
def make_orders():
    # MAIN CODE
    unit = "village"
    counselor = "caliph"
    food_list = ["quesadillas", "chips_and_salsa", "smores"]
    num_people = 10
    order1 = Order(unit, counselor, food_list, num_people)
    order1.get_order_needs()

    unit = "the hill"
    counselor = "tortuga"
    food_list = ["stir_fry", "veggies_and_hummus"]
    num_people = 20
    order2 = Order(unit, counselor, food_list, num_people, pickup_day=3, dropoff_day=4)
    order2.get_order_needs()

# This is true if the script is run by the interpreter, not imported by another
# module.
if __name__ == '__main__':
    # main should return 0 for success, something else (usually 1) for error.
    sys.exit(main())
