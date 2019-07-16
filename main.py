#! /usr/bin/env python
import sys
import tkinter as tk
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

    main_screen = tk.Tk()
    main_screen.title("Grubstake")
    pixel = tk.PhotoImage(width=1, height=1)

    #set window size
    w, h = main_screen.winfo_screenwidth(), main_screen.winfo_screenheight()
    main_screen.geometry("%dx%d+0+0" % (w/2, h/2))

    # code to add widgets
    frames_list = []
    button_list = []
    button_counter = 0
    num_buttons = 2

    for i in range(num_buttons):
        frames_list.append(tk.Frame(main_screen, width = 200, height = 200))
        frames_list[i].propagate(False)
        frames_list[i].grid(row = 0, column = i, sticky = "nsew", padx = 2, pady = 2)

    enter_order_button = tk.Button(frames_list[button_counter], text="Enter Order", image=pixel, compound="c")
    enter_order_button.pack(expand=True, fill="both")
    button_list.append(enter_order_button)
    button_counter += 1

    view_orders_button = tk.Button(frames_list[button_counter], text="View Orders", image=pixel, compound="c")
    view_orders_button.pack(expand=True, fill="both")
    button_list.append(view_orders_button)
    button_counter += 1

    # main_screen.resizable(width=False, height=False)
    main_screen.mainloop()


    # MAIN CODE
    # unit = "village"
    # counselor = "caliph"
    # food_list = ["quesadillas", "chips_and_salsa", "smores"]
    # order1 = Order(unit, counselor, food_list, 10)
    # order1.get_order_needs()
    #
    # unit = "the hill"
    # counselor = "tortuga"
    # food_list = ["stir_fry", "veggies_and_hummus"]
    # order2 = Order(unit, counselor, food_list, 10, pickup_day=3, dropoff_day=4)
    # order2.get_order_needs()


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
