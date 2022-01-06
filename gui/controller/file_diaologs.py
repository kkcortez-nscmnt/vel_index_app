
import tkinter as tk
from tkinter import filedialog

class DatFileDiolog():
    def _select_dat_file(self):
        self.filename = filedialog.askopenfilename(
            initialdir='/',
            title=' Select a .dat extension file.',
            filetype=(("dat files",".dat"),("all files", "."))
        )
        try:
            self.filename == True
            self.label_sl500_dat_path['text'] = self.filename
            return self.filename
        except ValueError:
            tk.messagebox.showerror('Information', "Error: File type.")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror('Information', f'No such file found.')
            return None

    def _select_vel_file(self):
        self.filename = filedialog.askopenfilename(
            initialdir='/',
            title=' Select a .dat extension file.',
            filetype=(("vel files",".vel"),("all files", "."))
        )
        try:
            self.filename == True
            self.label_sl500_vel_path['text'] = self.filename
            return self.filename
        except ValueError:
            tk.messagebox.showerror('Information', "Error: File type.")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror('Information', f'No such file found.')
            return None

    def _select_mat_file(self):
        self.filename = filedialog.askopenfilename(
            initialdir='/',
            title=' Select a .dat extension file.',
            filetype=(("vel files",".mat"),("all files", "."))
        )
        try:
            self.filename == True
            self.label_m9_path['text'] = self.filename
            return self.filename
        except ValueError:
            tk.messagebox.showerror('Information', "Error: File type.")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror('Information', f'No such file found.')
            return None
    