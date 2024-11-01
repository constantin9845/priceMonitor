import requests
import tkinter as tk
from gui import Frame
from data import Data



class App:
    def __init__(self, root):

        # create data object
        data = Data()
        t = data.return_basic()

        self.root = root
        self.root.title(t)

        # Create an instance of MyFrame from components module
        frame = Frame(self.root)
        frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()




# format of data

# Latest <name> Price:
# Date: 
# Time: 
# <name> Price: 
# percentage up or down: 