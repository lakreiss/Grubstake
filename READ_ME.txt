Purpose: Order database for Grubstake

How to use: enter orders, backend keeps track of all the data. Query for day or cabin-specific searches

How certain things work:
supplies are reused for different meals in a single order.
  e.g. if you order quesadillas and pancakes, you only need one stove
ingredients are combined together for each meal
  e.g. if you order quesadillas and breakfast burritos, you'll get twice as many tortillas as someone who is only getting quesadillas
each meal gives an estimated serving size for the quantity of items it lists.
these serving sizes are then divided by the number of people in the order, rounding up,
to determine the amount of food to serve


THINGS TO DO IN THE FUTURE
multipliers for different units
options *****
  make option types and numbers
    -use multi-select function
    -for each option selected, choose num_people
differentiate breakfast, dinner, misc.
make order input mechanical from text file
make times 15 minute intervals/more times
allow pickups a different session?
improve formatting and converting from backend -> frontend text
  ********
make options_per_line dependent on number of choices

GRUBSTAKE LAYOUT
main_menu -> enter order -> choose unit -> choose counselor -> session -> pickup day -> pickup time -> drop off day -> drop off time -> num people -> choose items -> options -> confirmation -> main menu
        '--> view orders -> choose day -> choose schedule or ingredients -> schedule (cabins) -> ingredients
                                                                      '---> ingredients


things to view:
schedule of pickup times with cabins
  each time slot has its own box, with counselors names in it
  clicking on the time slot shows you the cabin with their ingredients (and a return button)
each cabin's ingredients
each day's ingredients
