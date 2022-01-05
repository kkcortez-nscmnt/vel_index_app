import tkinter as tk
from tkinter import ttk


FONT = 11

class EntryDataFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        
        ##### LabelFrame arquivos sl500 #####
        self.label_sl500 = ttk.LabelFrame(self, text=" Load SL500 Data")
        self.label_sl500.place(rely=0.01, relx=0.009, height=90, width=460)

        ##### label path dos arquivos .dat #####
        self.label_sl500_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_path.place(rely=0.08, relx=0.19, height=23, width=367)
        # label path dos arquivos .vel
        self.label_sl500_path = ttk.Label(self.label_sl500, relief='ridge', anchor='w')
        self.label_sl500_path.place(rely=0.60, relx=0.19, height=23, width=367)
        # botão arquivo DAT
        self.btn_sl500_file = ttk.Button(self.label_sl500, padding=2, text='dat file') # todo command
        self.btn_sl500_file.place(rely=0.04, relx= 0.01)
        # botão arquivo VAL
        self.btn_sl500_file = ttk.Button(self.label_sl500, padding=2, text='vel file') # todo command
        self.btn_sl500_file.place(rely=0.55, relx= 0.01)

        ##### Label frame dos arquivos .mat #####
        self.label_m9 = ttk.LabelFrame(self, text=" Load M9 Data")
        self.label_m9.place(rely=0.175, relx=0.009, height=50, width=460)
        # label path dos arquivos .vel
        self.label_m9_path = ttk.Label(self.label_m9, relief='ridge', anchor='w')
        self.label_m9_path.place(rely=0.09,relx=0.19, height=23, width=367 )
        # botão arquivo .mat
        self.btn_m9_file = ttk.Button(self.label_m9, padding=2, text='mat file') #todo command
        self.btn_m9_file.place(rely=0.04,relx=0.01)
    
        

