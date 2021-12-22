import tkinter as tk
from gui.views.top_level_window import BaseWindow

BIO = "As intruções de uso serão postas aqui"

class HelpWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title("Instructions")
        
        frame_help = tk.LabelFrame(self.base_frame, text="User instruction")
        frame_help.pack(expand=True, fill="both")
        label_help = tk.Label(frame_help, text=BIO, font=self.fonts)
        label_help.pack(expand=True)