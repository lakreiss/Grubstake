import tkinter as tk, gui, sys, math

class GUI:
    def __init__(self):
        self.units_file_name = "camp_info/units.txt"
        self.open_main_menu_gui()

    def get_units_list(self):
        f = open(self.units_file_name, "r")
        fl = f.readlines()
        units_list = []
        for line in fl:
            units_list += [line.lower().replace(" ", "_").replace("\n", "")]
        return units_list

    def open_enter_order_gui(self, screen, frame_list, label_list, order_info={}):
        #TODO
        for frame in frame_list:
            frame.destroy()

        #get list of units
        units_list = self.get_units_list()

        frame_list = []
        label_list = []
        label_counter = 0
        num_labels = len(units_list)
        labels_per_line = 5
        num_lines = math.ceil(num_labels / labels_per_line)

        x_step = self.window_w / (labels_per_line)
        y_step = self.window_h / (num_labels / num_lines)
        for i in range(num_labels):
            frame_list.append(tk.Frame(screen, width = x_step, height = y_step))
            frame_list[i].propagate(False)
            frame_list[i].place(x = round((i % labels_per_line) * x_step), y = round((i // labels_per_line) * y_step))

            enter_order_label = tk.Label(frame_list[label_counter], text=units_list[i], compound="c")
            # enter_order_label.bind("<Button-" + str(i + 1) + ">", lambda e: self.open_choose_counselor_gui(screen, frame_list, label_list, order_info, units_list[i]))
            enter_order_label.bind("<Button>", lambda e, unit_name=units_list[i]: self.open_choose_counselor_gui(screen, frame_list, label_list, order_info, unit_name))
            enter_order_label.pack(expand=True, fill="both")
            label_list.append(enter_order_label)
            label_counter += 1

        # screen.quit()
        print("enter order clicked")

    def open_choose_counselor_gui(self, screen, frame_list, label_list, order_info, counselor=""):
        order_info["counselor"] = counselor
        print(counselor)

    def open_view_orders_gui(self, screen, frame_list, label_list):
        #TODO
        # for frame in frame_list:
        #     frame.destroy()
        # screen.quit()
        print("view orders clicked")

    def open_main_menu_gui(self, screen="", frame_list=""):
        if (frame_list is not ""):
            for frame in frame_list:
                frame.destroy()
            main_screen = screen
        else:
            main_screen = tk.Tk()
            main_screen.title("Grubstake")

        self.screen_w, self.screen_h = main_screen.winfo_screenwidth(), main_screen.winfo_screenheight()
        self.window_w, self.window_h = self.screen_w / 2, self.screen_h / 2

        #set window size
        main_screen.geometry("%dx%d+0+0" % (self.window_w, self.window_h))

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
        enter_order_label.bind("<Button>", lambda e: self.open_enter_order_gui(screen, frame_list, label_list))
        enter_order_label.pack(expand=True, fill="both")
        label_list.append(enter_order_label)
        label_counter += 1

        view_order_label = tk.Label(frame_list[label_counter], text="View Orders", compound="c")
        view_order_label.bind("<Button>", lambda e: self.open_view_orders_gui(screen, frame_list, label_list))
        view_order_label.pack(expand=True, fill="both")
        label_list.append(view_order_label)
        label_counter += 1


        # main_screen.resizable(width=False, height=False)
        main_screen.mainloop()
