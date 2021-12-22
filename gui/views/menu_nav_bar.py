import tkinter as tk

class Navbar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Help", command=parent.open_help_page) # todo command
        menu_file.add_command(label="About", command=parent.open_about_page) # todo command
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=parent.quit)

        