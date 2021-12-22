import tkinter as tk
from gui.views.top_level_window import BaseWindow

BIO = "A descrição a respeito da aplicação vem aqui"

class AboutWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title("About the application")
        
        frame_about = tk.LabelFrame(self.base_frame, text="App informations")
        frame_about.pack(expand=True, fill="both")
        label_about = tk.Label(frame_about, text=BIO, font=self.fonts)
        label_about.pack(expand=True)