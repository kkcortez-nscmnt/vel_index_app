import tkinter as tk
from tkinter import ttk
from gui.views.entry_data import EntryDataFrame
from gui.views.regression_frame import RegressionFrame
from gui.views.menu_nav_bar import Navbar

APP_HEIGHT = 600
APP_WIDTH = 1024

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HidroSedi - IVRC Module v1.0")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.menu_bar = Navbar(parent=self)
        self.config(menu=self.menu_bar)
        # criação do notebook
        self.notebook = ttk.Notebook(self)
        # instanciamento dos frames do notebook
        self.entry_data_frame = EntryDataFrame(self.notebook)
        self.regression_frame = RegressionFrame(self.notebook)
        # criação das abas do notebook
        self.notebook.add(self.entry_data_frame, text="Data config")
        self.notebook.add(self.regression_frame, text="Regression")
        # posição do notebook widget no tkframe
        self.notebook.place(x=0, y=0, width=APP_WIDTH, height=APP_HEIGHT)
    

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()



