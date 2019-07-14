#! /usr/bin/env python
import sys
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
    #
    # print("Hello, world")
    unit = "village"
    counselor = "caliph"
    food_list = ["quesadillas", "chipsandsalsa", "smores"]
    order1 = Order(unit, counselor, food_list, 10)
    order1.output_order_needs()
    #if an_error_occurred:
    #    return 'I\'m returning a string, it will be printed and 1 returned'
    #

    # Otherwise 0, success is returned.
    return 0

# This is true if the script is run by the interpreter, not imported by another
# module.
if __name__ == '__main__':
    # main should return 0 for success, something else (usually 1) for error.
    sys.exit(main())
