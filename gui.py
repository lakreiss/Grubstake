import tkinter as tk, gui, sys, math, order, random

class GUI:
    def __init__(self):
        self.max_labels_per_line = 4
        self.units_file_name = "camp_info/units.txt"
        self.units_folder_name = "camp_info/units/"
        self.sessions_file_name = "camp_info/sessions.txt"
        self.days_of_session_file_name = "camp_info/days.txt"
        self.time_options_file_name = "camp_info/time_options.txt"
        self.num_people_options_file_name = "camp_info/num_people_options.txt"
        self.boolean_options_file_name = "camp_info/boolean_options.txt"
        self.menu_options_file_name = "meals/all_meals.txt"
        self.main_menu_gui()

    #*********************END INIT, BEGIN ORDER ENTRY*********************

    def choose_unit_gui(self, screen, frame_list, label_list, order_info):
        screen_name = "Choose Unit"

        path = self.units_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, unit_name: self.choose_counselor_gui(screen, frame_list, label_list, order_info, unit_name)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.main_menu_gui(False, screen, frame_list, label_list)

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_counselor_gui(self, screen, frame_list, label_list, order_info, unit):
        order_info["unit"] = unit
        print(unit)

        screen_name = "Choose Counselor"

        path = self.units_folder_name + unit + ".txt"
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, counselor: self.choose_session_gui(screen, frame_list, label_list, order_info, counselor)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_unit_gui(screen, frame_list, label_list, order_info)

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_session_gui(self, screen, frame_list, label_list, order_info, counselor):
        order_info["counselor"] = counselor
        print(counselor)

        screen_name = "Choose Session"

        path = self.sessions_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, session: self.choose_pickup_day_gui(screen, frame_list, label_list, order_info, session)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_counselor_gui(screen, frame_list, label_list, order_info, order_info["unit"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_pickup_day_gui(self, screen, frame_list, label_list, order_info, session):
        order_info["session"] = session
        print(session)

        screen_name = "Choose Pickup Day"

        path = self.days_of_session_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, pickup_day: self.choose_pickup_time_gui(screen, frame_list, label_list, order_info, pickup_day)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_session_gui(screen, frame_list, label_list, order_info, order_info["counselor"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_pickup_time_gui(self, screen, frame_list, label_list, order_info, pickup_day):
        order_info["pickup_day"] = pickup_day
        print(pickup_day)

        screen_name = "Choose Pickup Time"

        path = self.time_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, pickup_time: self.choose_drop_off_day_gui(screen, frame_list, label_list, order_info, pickup_time)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_pickup_day_gui(screen, frame_list, label_list, order_info, order_info["session"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_drop_off_day_gui(self, screen, frame_list, label_list, order_info, pickup_time):
        order_info["pickup_time"] = pickup_time
        print(pickup_time)

        screen_name = "Choose Drop-Off Day"

        path = self.days_of_session_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, drop_off_day: self.choose_drop_off_time_gui(screen, frame_list, label_list, order_info, drop_off_day)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_pickup_time_gui(screen, frame_list, label_list, order_info, order_info["pickup_day"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_drop_off_time_gui(self, screen, frame_list, label_list, order_info, drop_off_day):
        order_info["drop_off_day"] = drop_off_day
        print(drop_off_day)

        screen_name = "Choose Drop-Off Time"

        path = self.time_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, drop_off_day: self.choose_number_of_people(screen, frame_list, label_list, order_info, drop_off_day)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_drop_off_day_gui(screen, frame_list, label_list, order_info, order_info["pickup_time"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_number_of_people(self, screen, frame_list, label_list, order_info, drop_off_time):
        order_info["drop_off_time"] = drop_off_time
        print(drop_off_time)

        screen_name = "Choose Number of People"

        path = self.num_people_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, drop_off_time: self.choose_items_gui(screen, frame_list, label_list, order_info, drop_off_time)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_drop_off_time_gui(screen, frame_list, label_list, order_info, order_info["drop_off_day"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def choose_items_gui(self, screen, frame_list, label_list, order_info, num_people):
        order_info["num_people"] = num_people
        print(num_people)

        screen_name = "Choose Items"

        path = self.menu_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        items_chosen = []

        next_page_func = lambda screen, frame_list, label_list, order_info, item_list: self.choose_options_gui(screen, frame_list, label_list, order_info, item_list)
        same_page_func = lambda screen, frame_list, label_list, order_info, items_chosen, chosen_item: self.make_multi_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, same_page_func, prev_page_func, items_chosen, chosen_item)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_number_of_people(screen, frame_list, label_list, order_info, order_info["drop_off_time"])

        self.make_multi_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, same_page_func, prev_page_func, items_chosen)

    #TODO: improve for more complicated options-entries (already made text file)
    def choose_options_gui(self, screen, frame_list, label_list, order_info, item_list):
        order_info["item_list"] = item_list
        print(item_list)

        screen_name = "Are There Options?"

        path = self.boolean_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, options: self.confirmation_page_gui(screen, frame_list, label_list, order_info, options)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_items_gui(screen, frame_list, label_list, order_info, order_info["num_people"])

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func)

    def confirmation_page_gui(self, screen, frame_list, label_list, order_info, options):
        if options == "yes":
            order_info["needs_options"] = True
        elif options == "no":
            order_info["needs_options"] = False
        else:
            print("ERROR IN OPTIONS")
        print(order_info["needs_options"])

        all_keys = []
        for key in order_info:
            all_keys += [key]
        all_keys.sort()

        screen_text = "\nHere's what I have for your order so far:\n\n"
        for key in all_keys:
            screen_text += key.replace("_", " ") + " = " + str(order_info[key]).replace("_", " ") + "\n"

        screen_text += "\nIs this correct?\n"
        text_height = 20 * (len(order_info) + 3)

        path = self.boolean_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, answer: self.make_order(screen, frame_list, label_list, order_info, answer)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_options_gui(screen, frame_list, label_list, order_info, order_info["item_list"])

        self.make_one_click_gui(screen, screen_text, frame_list, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func, text_height=text_height)

    def make_order(self, screen, frame_list, label_list, order_info, answer):
        if answer == "yes":
            order.Order(order_info["unit"], order_info["counselor"], order_info["item_list"], order_info["num_people"], order_info["session"], order_info["pickup_day"], order_info["pickup_time"], order_info["drop_off_day"], order_info["drop_off_time"], order_info["needs_options"])
            self.main_menu_gui(False, screen, frame_list, label_list)
        elif answer == "no":
            self.choose_unit_gui(screen, frame_list, label_list, {})
        else:
            print("ERROR IN CONFIRMATION PAGE")

    #*********************END ORDER ENTRY, BEGIN VIEW ORDERS*********************

    def choose_view_session_gui(self, screen, frame_list, label_list, view_info):
        screen_name = "Choose Session to View"

        path = self.sessions_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, view_info, choice: self.choose_view_day_gui(screen, frame_list, label_list, view_info, choice)
        prev_page_func = lambda screen, frame_list, label_list, view_info: self.main_menu_gui(False, screen, frame_list, label_list)

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, view_info, next_page_func, prev_page_func)

    def choose_view_day_gui(self, screen, frame_list, label_list, view_info, session):
        view_info["session"] = session
        print(session)

        screen_name = "Choose Day to View"

        path = self.days_of_session_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, view_info, choice: self.choose_view_type_gui(screen, frame_list, label_list, view_info, choice)
        prev_page_func = lambda screen, frame_list, label_list, view_info: self.choose_view_session_gui(screen, frame_list, label_list, view_info)

        self.make_one_click_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, view_info, next_page_func, prev_page_func)

    def choose_view_type_gui(self, screen, frame_list, label_list, view_info, day):
        view_info["day"] = day
        print(day)

        frontend_list = []
        backend_list = []
        color_list = []
        lambda_list = []

        screen_name = "Would You Like to View Day " + day + "\'s Schedule or Ingredients?"
        schedule_lambda = lambda screen, frame_list, label_list: lambda e: self.schedule_gui(screen, frame_list, label_list, view_info)
        ingredients_lambda = lambda screen, frame_list, label_list: lambda e: self.ingredients_gui(screen, frame_list, label_list, view_info)
        return_lambda = lambda screen, frame_list, label_list: lambda e: self.choose_view_day_gui(screen, frame_list, label_list, view_info, view_info["session"])

        #schedule_gui
        frontend_list += ["View Schedule"]
        backend_list += ["view_schedule"]
        color_list += ["lightblue"]
        lambda_list += [schedule_lambda]

        #ingredients_gui
        frontend_list += ["View Ingredients"]
        backend_list += ["view_ingredients"]
        color_list += ["lightgreen"]
        lambda_list += [ingredients_lambda]

        #return_gui
        frontend_list += ["Return"]
        backend_list += ["return"]
        color_list += ["red"]
        lambda_list += [return_lambda]

        self.make_multi_path_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, lambda_list)

    def schedule_gui(self, screen, frame_list, label_list, view_info):
        screen_name = "Session " + view_info["session"] + " Day " + view_info["day"] + " Schedule"

        path = self.time_options_file_name
        frontend_list, backend_list, color_list = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, view_info, time_slot, counselors_at_time_slot: self.view_ingredients_gui(screen, frame_list, label_list, view_info, time_slot, counselors_at_time_slot)
        prev_page_func = lambda screen, frame_list, label_list, view_info: self.choose_view_type_gui(screen, frame_list, label_list, view_info, view_info["day"])

        self.make_schedule_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, view_info, next_page_func, prev_page_func)

    def view_ingredients_gui(self, screen, frame_list, label_list, view_info, time_slot, counselors_at_time_slot):
        screen_text = "Here's what you need at " + time_slot + " on Day " + view_info["day"] + ":"

        text_list = []
        for counselor in counselors_at_time_slot:
            text_list += [order.Order.get_order_needs(counselor, view_info["session"], view_info["day"])]

        prev_page_func = lambda screen, frame_list, label_list, view_info: self.schedule_gui(screen, frame_list, label_list, view_info)

        self.make_text_with_return_gui(screen, screen_text, frame_list, view_info, text_list, prev_page_func)

    #*********************END VIEW ORDERS, BEGIN GUI TEMPLATES*********************

    def make_text_with_return_gui(self, screen, text, old_frames, info, text_list, prev_page_func, text_height=50, return_height=50):
        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        num_options = len(text_list)
        num_labels = num_options
        labels_per_line = num_options
        num_lines = math.ceil(num_labels / labels_per_line)

        border = 2
        title_height = text_height
        labels_height = self.window_h - title_height - return_height #save space for title
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = labels_height / num_lines - border

        #display each counselors' ingredients
        for i in range(num_options):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)) + title_height)

            option_label = tk.Label(frame_list[i], text=text_list[i], compound="c")
            option_label.config(bg="gray")
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #back button
        frame_list.append(tk.Frame(screen, width = self.window_w, height = return_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = labels_height + title_height)

        option_label = tk.Label(frame_list[i], text="Return", compound="c")
        option_label.bind("<Button>", lambda e: prev_page_func(screen, frame_list, label_list, info))
        option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

        #title/instructions
        frame_list.append(tk.Frame(screen, width = self.window_w, height = title_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = 0)

        option_label = tk.Label(frame_list[i], text=text, compound="c")
        # option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

    def make_schedule_gui(self, screen, text, old_frames, frontend_list, backend_list, color_list, info, next_page_func, prev_page_func, text_height=50, return_height=50):
        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        num_options = len(frontend_list)
        labels_per_line = min(self.max_labels_per_line, num_options)
        num_lines = math.ceil(num_options / labels_per_line)

        border = 2
        title_height = text_height
        labels_height = self.window_h - title_height - return_height #save space for title
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = labels_height / num_lines - border

        for i in range(num_options):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)) + title_height)

            counselors_at_time_slot = self.get_counselors_at_time_slot(backend_list[i], info)
            schedule_text = self.get_schedule_text(frontend_list[i], counselors_at_time_slot)

            option_label = tk.Label(frame_list[i], text=schedule_text, compound="c", anchor="n")
            if len(counselors_at_time_slot) > 0:
                option_label.bind("<Button>", lambda e, backend_name=backend_list[i], counselors=counselors_at_time_slot: next_page_func(screen, frame_list, label_list, info, backend_name, counselors))
            option_label.config(bg=color_list[i])
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #back button
        frame_list.append(tk.Frame(screen, width = self.window_w, height = return_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = labels_height + title_height)

        option_label = tk.Label(frame_list[i], text="Return", compound="c")
        option_label.bind("<Button>", lambda e: prev_page_func(screen, frame_list, label_list, info))
        option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

        #title/instructions
        frame_list.append(tk.Frame(screen, width = self.window_w, height = title_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = 0)

        option_label = tk.Label(frame_list[i], text=text, compound="c")
        # option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

    def make_one_click_gui(self, screen, text, old_frames, frontend_list, backend_list, color_list, info, next_page_func, prev_page_func, text_height=50, return_height=50):
        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        num_options = len(frontend_list)
        labels_per_line = min(self.max_labels_per_line, num_options)
        num_lines = math.ceil(num_options / labels_per_line)

        border = 2
        title_height = text_height
        labels_height = self.window_h - title_height - return_height#save space for title
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = labels_height / num_lines - border

        for i in range(num_options):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)) + title_height)

            option_label = tk.Label(frame_list[i], text=frontend_list[i], compound="c")
            option_label.bind("<Button>", lambda e, backend_name=backend_list[i]: next_page_func(screen, frame_list, label_list, info, backend_name))
            option_label.config(bg=color_list[i])
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #back button
        frame_list.append(tk.Frame(screen, width = self.window_w, height = return_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = labels_height + title_height)

        option_label = tk.Label(frame_list[i], text="Return", compound="c")
        option_label.bind("<Button>", lambda e: prev_page_func(screen, frame_list, label_list, info))
        option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

        #title/instructions
        frame_list.append(tk.Frame(screen, width = self.window_w, height = title_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = 0)

        option_label = tk.Label(frame_list[i], text=text, compound="c")
        # option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

    def make_multi_click_gui(self, screen, screen_name, old_frames, frontend_list, backend_list, color_list, info, next_page_func, same_page_func, prev_page_func, items_chosen=[], chosen_item="", text_height=50, return_height=50):
        if chosen_item is not "":
            if chosen_item in items_chosen:
                items_chosen.remove(chosen_item)
            else:
                items_chosen += [chosen_item]

        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        num_options = len(frontend_list)
        labels_per_line = min(self.max_labels_per_line, num_options)
        num_lines = math.ceil(num_options / labels_per_line)

        border = 2
        title_height = text_height
        labels_height = self.window_h - title_height - return_height #save space for title
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = labels_height / num_lines - border

        for i in range(num_options):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)) + title_height)

            option_label = tk.Label(frame_list[i], text=frontend_list[i], compound="c")
            option_label.bind("<Button>", lambda e, backend_name=backend_list[i]: same_page_func(screen, frame_list, label_list, info, items_chosen, backend_name))
            if (backend_list[i] in items_chosen):
                option_label.config(bg="gray")
            else:
                option_label.config(bg=color_list[i])
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #back button
        frame_list.append(tk.Frame(screen, width = self.window_w / 2 - border, height = return_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = labels_height + title_height)

        option_label = tk.Label(frame_list[i], text="Return", compound="c")
        option_label.bind("<Button>", lambda e: prev_page_func(screen, frame_list, label_list, info))
        option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

        #done button
        frame_list.append(tk.Frame(screen, width = self.window_w / 2 - border, height = return_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = self.window_w / 2, y = labels_height + title_height)

        option_label = tk.Label(frame_list[i], text="Done", compound="c")
        option_label.bind("<Button>", lambda e, item_list=items_chosen: next_page_func(screen, frame_list, label_list, info, item_list))
        option_label.config(bg="green")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

        #title/instructions
        frame_list.append(tk.Frame(screen, width = self.window_w, height = title_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = 0)

        option_label = tk.Label(frame_list[i], text=screen_name, compound="c")
        # option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

    def make_multi_path_gui(self, screen, screen_name, old_frames, frontend_list, backend_list, color_list, lambda_list, info={}, text_height=50, return_height=50):

        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        has_return_button = "Return" in frontend_list
        if (has_return_button):
            return_index = frontend_list.index("Return")
            return_lambda = lambda_list.pop(return_index)
            return_frontend = frontend_list.pop(return_index)
            return_backend = backend_list.pop(return_index)
        else:
            return_height = 0
        num_labels = len(frontend_list)
        labels_per_line = min(self.max_labels_per_line, num_labels)
        num_lines = math.ceil(num_labels / labels_per_line)

        border = 2
        title_height = text_height
        labels_height = self.window_h - title_height - return_height #save space for title
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = labels_height / num_lines - border

        for i in range(num_labels):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)) + title_height)

            option_label = tk.Label(frame_list[i], text=frontend_list[i], compound="c")
            option_label.bind("<Button>", lambda_list[i](screen, frame_list, label_list))
            option_label.config(bg=color_list[i])
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        if (has_return_button):
            #back button
            frame_list.append(tk.Frame(screen, width = self.window_w, height = return_height))
            i = len(frame_list) - 1
            frame_list[i].propagate(False)
            frame_list[i].place(x = 0, y = labels_height + title_height)

            option_label = tk.Label(frame_list[i], text=return_frontend, compound="c")
            option_label.bind("<Button>", return_lambda(screen, frame_list, label_list))
            option_label.config(bg="red")
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #title/instructions
        frame_list.append(tk.Frame(screen, width = self.window_w, height = title_height))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = 0, y = 0)

        option_label = tk.Label(frame_list[i], text=screen_name, compound="c")
        # option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)

    #*********************END GUI TEMPLATES, BEGIN MAIN GUIS*********************

    def main_menu_gui(self, new_menu=True, screen="", frame_list=[], label_list=[]):

        if new_menu:
            screen = tk.Tk()
            screen.title("Grubstake")

            self.screen_w, self.screen_h = screen.winfo_screenwidth(), screen.winfo_screenheight()
            self.window_w, self.window_h = self.screen_w  * 2 / 3, self.screen_h - 100

            #set window size
            screen.geometry("%dx%d+0+0" % (self.window_w, self.window_h))

        frontend_list = []
        backend_list = []
        color_list = []
        lambda_list = []

        screen_name = "Main Menu"
        enter_order_lambda = lambda screen, frame_list, label_list: lambda e: self.enter_order_gui(screen, frame_list, label_list, new_order=True)
        view_orders_lambda = lambda screen, frame_list, label_list: lambda e: self.view_orders_gui(screen, frame_list, label_list)

        #enter_order_gui
        frontend_list += ["Enter Order"]
        backend_list += ["enter_order"]
        color_list += ["lightblue"]
        lambda_list += [enter_order_lambda]

        #view_orders_gui
        frontend_list += ["View Orders"]
        backend_list += ["view_orders"]
        color_list += ["lightgreen"]
        lambda_list += [view_orders_lambda]

        self.make_multi_path_gui(screen, screen_name, frame_list, frontend_list, backend_list, color_list, lambda_list)

        if new_menu:
            # screen.resizable(width=False, height=False)
            screen.mainloop()

    def enter_order_gui(self, screen, frame_list, label_list, order_info={}, new_order=False):
        #broke this up into two parts for naming clarity
        if new_order:
            order_info = {}
        self.choose_unit_gui(screen, frame_list, label_list, order_info)

    def view_orders_gui(self, screen, frame_list, label_list, view_info={}):
        #broke this up into two parts for naming clarity
        self.choose_view_session_gui(screen, frame_list, label_list, view_info)

    #*********************END GUIS, BEGIN BACKEND PROCESSING*********************

    def get_counselors_at_time_slot(self, time_slot, info):
        file_path = "orders/session_" + info["session"] + "/day_" + info["day"] + ".txt"

        f = open(file_path, "r")
        fl = f.readlines()
        counselor_list = []
        for line in fl:
            if ("pickup_time " + time_slot) in line:
                #hacky way to get the counselor
                counselor_section, rest = line.split(", drop_off_day")
                title, counselor = counselor_section.split(" ")
                counselor_list += [counselor]

        return counselor_list

    def get_schedule_text(self, time_slot, counselors_at_time_slot):
        schedule_text = time_slot
        for counselor in counselors_at_time_slot:
            schedule_text += counselor.replace("_", " ") + "\n"
        return schedule_text

    #returns a frontend list and backend list, along with colors
    #text file must have entries of form: name-color
    def get_list_and_colors(self, path):
        f = open(path, "r")
        fl = f.readlines()
        frontend_list = []
        backend_list = []
        color_list = []
        for line in fl:
            if ("-") in line:
                unit, color = line.split("-")
                frontend_list += [unit]
                backend_list += [unit.lower().replace(" ", "_").replace("\n", "")]
                color_list += [color.lower().replace(" ", "").replace("\n", "")]
            else:
                #default is gray
                unit = line
                color = self.get_random_color()
                frontend_list += [unit]
                backend_list += [unit.lower().replace(" ", "_").replace("\n", "")]
                color_list += [color]

        return frontend_list, backend_list, color_list

    def get_random_color(self):
        letter_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        color_name = "#"
        for i in range(6):
            color_name += letter_list[random.randint(0, len(letter_list) - 1)]
        return color_name
