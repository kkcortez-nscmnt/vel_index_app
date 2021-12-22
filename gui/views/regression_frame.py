import tkinter as tk
from tkinter import ttk

class RegressionFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.LabelB = ttk.Label(self, text="Regression Frame")
        self.LabelB.grid(column=1, row=1)
