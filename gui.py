import tkinter as tk
from data import Data

class Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.data = Data()
        self.gen_initial_window(self.data.return_basic())


    def gen_initial_window(self, initial_data):




        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

