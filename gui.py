import tkinter as tk, gui, sys

class GUI:
    def __init__(self):
        self.open_main_menu_gui()

    def open_enter_order_gui(self, screen, frames_list):
        #TODO
        for frame in frames_list:
            frame.destroy()
        # screen.quit()
        print("hello, world")

    def open_main_menu_gui(self, screen="", frames_list=""):
        if (frames_list is not ""):
            for frame in frames_list:
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
        frames_list = []
        button_list = []
        button_counter = 0
        num_buttons = 2

        for i in range(num_buttons):
            frames_list.append(tk.Frame(main_screen, width = (self.window_w / num_buttons) - (2 * num_buttons), height = self.window_h - 2))
            frames_list[i].propagate(False)
            frames_list[i].grid(row = 0, column = i, sticky = "nsew", padx = 2, pady = 2)

        enter_order_button = tk.Button(frames_list[button_counter], text="Enter Order", image=self.pixel, compound="c")
        enter_order_button.pack(expand=True, fill="both")
        enter_order_button.config(command = lambda: self.open_enter_order_gui(main_screen, frames_list))
        button_list.append(enter_order_button)
        button_counter += 1

        view_orders_button = tk.Button(frames_list[button_counter], text="View Orders", image=self.pixel, compound="c")
        view_orders_button.pack(expand=True, fill="both")
        button_list.append(view_orders_button)
        button_counter += 1

        # main_screen.resizable(width=False, height=False)
        main_screen.mainloop()
