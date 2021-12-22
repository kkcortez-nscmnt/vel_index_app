import tkinter as tk

FONT_SIZE = 9
WINDOW_WIDTH = 600
WINDOW_HIGHT = 900

class BaseWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.base_frame = tk.Frame(self)
        self.base_frame.pack_propagate(0)
        self.base_frame.pack(fill="both", expand=True)
        self.fonts = ("Trebuchet MS",FONT_SIZE )
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HIGHT}")
        self.resizable(0, 0)
