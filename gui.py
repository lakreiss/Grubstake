import tkinter as tk, gui, sys

class GUI:
    def __init__(self):
        self.open_main_menu_gui()

    def open_enter_order_gui(self, screen, frame_list, label_list):
        #TODO
        for frame in frame_list:
            frame.destroy()
        # screen.quit()
        print("hello, world")

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
        self.pixel = tk.PhotoImage(width=1, height=1)

        #set window size
        main_screen.geometry("%dx%d+0+0" % (self.window_w, self.window_h))

        # code to add widgets
        frame_list = []
        label_list = []
        label_counter = 0
        num_labels = 2

        for i in range(num_labels):
            frame_list.append(tk.Frame(main_screen, width = (self.window_w / num_labels) - (2 * num_labels), height = self.window_h - 2))
            frame_list[i].propagate(False)
            frame_list[i].grid(row = 0, column = i, sticky = "nsew", padx = 2, pady = 2)

        enter_order_label = tk.Label(frame_list[label_counter], text="Enter Orders", width=100, height=100, compound="center")
        enter_order_label.bind("<Button>", lambda e: self.open_enter_order_gui(screen, frame_list, label_list))
        enter_order_label.pack(expand=True, fill="both")
        label_list.append(enter_order_label)
        label_counter += 1

        view_orders_label = tk.Label(frame_list[label_counter], text="View Orders", image=self.pixel, compound="c")
        view_orders_label.pack(expand=True, fill="both")
        label_list.append(view_orders_label)
        label_counter += 1

        # main_screen.resizable(width=False, height=False)
        main_screen.mainloop()
