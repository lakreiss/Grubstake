import tkinter as tk, gui, sys, math

class GUI:
    def __init__(self):
        self.units_file_name = "camp_info/units.txt"
        self.units_folder_name = "camp_info/units/"
        self.sessions_file_name = "camp_info/sessions.txt"
        self.main_menu_gui()

    #returns a frontend list and backend list, along with colors
    #text file must have entries of form: name-color
    def get_list_and_colors(self, path):
        f = open(path, "r")
        fl = f.readlines()
        list_frontend = []
        list_backend = []
        color_list = []
        for line in fl:
            if ("-") in line:
                unit, color = line.split("-")
                list_frontend += [unit]
                list_backend += [unit.lower().replace(" ", "_").replace("\n", "")]
                color_list += [color.lower().replace(" ", "").replace("\n", "")]
            else:
                #default is gray
                unit = line
                color = "gray"
                list_frontend += [unit]
                list_backend += [unit.lower().replace(" ", "_").replace("\n", "")]
                color_list += [color]

        return list_frontend, list_backend, color_list

    def enter_order_gui(self, screen, frame_list, label_list, order_info={}):
        self.choose_unit_gui(screen, frame_list, label_list, order_info)


    def choose_unit_gui(self, screen, frame_list, label_list, order_info):
        unit_list_frontend, unit_list_backend, unit_colors = self.get_list_and_colors(self.units_file_name)

        next_page_func = lambda screen, frame_list, label_list, order_info, unit_name: self.choose_counselor_gui(screen, frame_list, label_list, order_info, unit_name)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.main_menu_gui(False, screen, frame_list, label_list)

        self.make_gui(screen, frame_list, unit_list_frontend, unit_list_backend, unit_colors, order_info, next_page_func, prev_page_func)

    def choose_counselor_gui(self, screen, frame_list, label_list, order_info, unit):
        order_info["unit"] = unit
        print(unit)

        #get list of counselors
        path = self.units_folder_name + unit + ".txt"
        counselor_list_frontend, counselor_list_backend, counselor_colors = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, counselor: self.choose_session_gui(screen, frame_list, label_list, order_info, counselor)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_unit_gui(screen, frame_list, label_list, order_info)

        self.make_gui(screen, frame_list, counselor_list_frontend, counselor_list_backend, counselor_colors, order_info, next_page_func, prev_page_func)

    def choose_session_gui(self, screen, frame_list, label_list, order_info, counselor):
        order_info["counselor"] = counselor
        print(counselor)

        #get list of sessions
        path = self.sessions_file_name
        counselor_list_frontend, counselor_list_backend, counselor_colors = self.get_list_and_colors(path)

        next_page_func = lambda screen, frame_list, label_list, order_info, counselor: self.choose_session_gui(screen, frame_list, label_list, order_info, counselor)
        prev_page_func = lambda screen, frame_list, label_list, order_info: self.choose_unit_gui(screen, frame_list, label_list, order_info)

    def make_gui(self, screen, old_frames, frontend_list, backend_list, color_list, order_info, next_page_func, prev_page_func):
        for frame in old_frames:
            frame.destroy()

        frame_list = []
        label_list = []
        num_options = len(frontend_list)
        num_labels = num_options + 1
        labels_per_line = 4
        num_lines = math.ceil(num_labels / labels_per_line)

        border = 2
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = self.window_h / num_lines - border
        for i in range(num_options):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)))

            option_label = tk.Label(frame_list[i], text=frontend_list[i], compound="c")
            option_label.bind("<Button>", lambda e, backend_name=backend_list[i]: next_page_func(screen, frame_list, label_list, order_info, backend_name))
            option_label.config(bg=color_list[i])
            option_label.pack(expand=True, fill="both")
            label_list.append(option_label)

        #back button
        frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)))

        option_label = tk.Label(frame_list[i], text="Return", compound="c")
        option_label.bind("<Button>", lambda e: prev_page_func(screen, frame_list, label_list, order_info))
        option_label.config(bg="red")
        option_label.pack(expand=True, fill="both")
        label_list.append(option_label)
        i += 1

    def view_orders_gui(self, screen, frame_list, label_list):
        #TODO
        # for frame in frame_list:
        #     frame.destroy()
        # screen.quit()
        print("view orders clicked")

    def main_menu_gui(self, new_menu=True, screen="", frame_list="", label_list=""):

        if new_menu:
            main_screen = tk.Tk()
            main_screen.title("Grubstake")

            self.screen_w, self.screen_h = main_screen.winfo_screenwidth(), main_screen.winfo_screenheight()
            self.window_w, self.window_h = self.screen_w / 2, self.screen_h / 2

            #set window size
            main_screen.geometry("%dx%d+0+0" % (self.window_w, self.window_h))
        else:
            if (frame_list is not ""):
                for frame in frame_list:
                    frame.destroy()
                main_screen = screen

        # code to add widgets
        frame_list = []
        label_list = []
        label_counter = 0
        num_labels = 2

        x_step = self.window_w / num_labels
        for i in range(num_labels):
            frame_list.append(tk.Frame(main_screen, width = (self.window_w / num_labels) - (2 * num_labels), height = self.window_h - 2))
            frame_list[i].propagate(False)
            frame_list[i].place(x = i * x_step, y = 0)

        enter_order_label = tk.Label(frame_list[label_counter], text="Enter Orders", compound="c")
        enter_order_label.bind("<Button>", lambda e: self.enter_order_gui(screen, frame_list, label_list))
        enter_order_label.pack(expand=True, fill="both")
        label_list.append(enter_order_label)
        label_counter += 1

        view_order_label = tk.Label(frame_list[label_counter], text="View Orders", compound="c")
        view_order_label.bind("<Button>", lambda e: self.view_orders_gui(screen, frame_list, label_list))
        view_order_label.pack(expand=True, fill="both")
        label_list.append(view_order_label)
        label_counter += 1

        if new_menu:
            # main_screen.resizable(width=False, height=False)
            main_screen.mainloop()

    #obsolete
    def enter_order_gui_OLD(self, screen, frame_list, label_list, order_info={}):

        #get list of units
        unit_list_frontend, unit_list_backend, unit_colors = self.get_list_and_colors(self.units_file_name)

        frame_list = []
        label_list = []
        num_units = len(unit_list_frontend)
        num_labels = num_units + 1
        labels_per_line = 4
        num_lines = math.ceil(num_labels / labels_per_line)

        border = 2
        x_step = (self.window_w / (labels_per_line)) - border
        y_step = self.window_h / num_lines - border
        for i in range(num_units):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)))

            enter_order_label = tk.Label(frame_list[i], text=unit_list_frontend[i], compound="c")
            # enter_order_label.bind("<Button-" + str(i + 1) + ">", lambda e: self.choose_counselor_gui(screen, frame_list, label_list, order_info, unit_list_frontend[i]))
            enter_order_label.bind("<Button>", lambda e, unit_name=unit_list_backend[i]: self.choose_counselor_gui(screen, frame_list, label_list, order_info, unit_name))
            enter_order_label.config(bg=unit_colors[i])
            enter_order_label.pack(expand=True, fill="both")
            label_list.append(enter_order_label)

        #back button
        frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
        i = len(frame_list) - 1
        frame_list[i].propagate(False)
        frame_list[i].place(x = round((i % labels_per_line) * (x_step + 2)), y = round((i // labels_per_line) * (y_step + 2)))

        enter_order_label = tk.Label(frame_list[i], text="Return", compound="c")
        # enter_order_label.bind("<Button-" + str(i + 1) + ">", lambda e: self.choose_counselor_gui(screen, frame_list, label_list, order_info, unit_list_frontend[i]))
        enter_order_label.bind("<Button>", lambda e: self.main_menu_gui(False, screen, frame_list, label_list))
        enter_order_label.config(bg="red")
        enter_order_label.pack(expand=True, fill="both")
        label_list.append(enter_order_label)
        i += 1

        # screen.quit()
        print("enter order clicked")
