import tkinter as tk
from tkinter import ttk


class EntryDataFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.labelA = ttk.Label(self, text="Entry Data Frame")
        self.labelA.grid(column=1, row=1)

