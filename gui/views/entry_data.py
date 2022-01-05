import tkinter as tk
from tkinter import ttk


FONT = 11

class EntryDataFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        # label arquivos sl500
        self.label_sl500 = ttk.LabelFrame(self, text="SL500 Data",)
        self.label_sl500.place(rely=0.01, relx=0.009, height=150, width=460)
        # label path dos arquivos .dat
        self.label_sl500_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_path.place(rely=0.03, relx=0.19, height=23, width=367)
        # label path dos arquivos .vel
        self.label_sl500_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_path.place(rely=0.29, relx=0.19, height=23, width=367)
        # botão arquivo DAT
        self.btn_sl500_file = ttk.Button(self, padding=2, text='Load .dat file') # todo command
        self.btn_sl500_file.place(rely=0.04, relx= 0.01)
        # botão arquivo VAL
        self.btn_sl500_file = ttk.Button(self, padding=2, text='Load .vel file') # todo command
        self.btn_sl500_file.place(rely=0.1, relx= 0.01)
        

