import tkinter as tk
from tkinter import INSERT
from datetime import date

from data import Data

# generate starting window
class App:
    def __init__(self, root):
        self.root = root
        self.data = Data()  # used to all data calls
        self.date = date.today()

        self.root.title("Report")
        self.root.geometry("400x700")
        self.root.configure(bg="lightyellow")


        self.create_widgets()
        self.start_data()

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="lightgray")
        header_frame.pack(fill="x")

        # Date label
        self.date_label = tk.Label(self.root, text="Base Currency : "+self.data.get_status()[0]+"\t"+str(self.date), font=("Arial", 10), bg="lightyellow")
        self.date_label.pack()

        # box with data boxes
        data_frame = tk.Frame(self.root, bg="lightblue")
        data_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        # Text box currencies
        frame1 = tk.Frame(data_frame)
        frame1.grid(row=0, column=0, pady=3)
        label1 = tk.Label(frame1, text="Currency")
        label1.pack(side=tk.TOP)
        self.currencies = tk.Text(frame1, wrap=tk.WORD, bg="white", fg="black", height=10, width=40)
        self.currencies.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Text box assets
        frame2 = tk.Frame(data_frame)
        frame2.grid(row=1, column=0, pady=3)
        label2 = tk.Label(frame2, text="Assets")
        label2.pack(side=tk.TOP)
        self.assets = tk.Text(frame2, wrap=tk.WORD, bg="white", fg="black", height=10, width=40)
        self.assets.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Text box securities
        frame3 = tk.Frame(data_frame)
        frame3.grid(row=2, column=0, pady=3)
        label3 = tk.Label(frame3, text="Securities")
        label3.pack(side=tk.TOP)
        self.securities = tk.Text(frame3, wrap=tk.WORD, bg="white", fg="black", height=10, width=40)
        self.securities.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Button frame
        button_frame = tk.Frame(self.root, bg="lightyellow")
        button_frame.pack(fill="x", side="bottom", pady=10)

        # Search button
        search_button = tk.Button(button_frame, text="Search", width=10, command=self.search)
        search_button.pack(side="left", padx=10)

        # Refresh button with update command
        refresh_button = tk.Button(button_frame, text="Refresh", width=10)
        refresh_button.pack(side="right", padx=10)

    def search(self):
        self.display_search()

    def display_search(self):
        self.overlay_frame = tk.Frame(self.root, bg="lightgray")
        self.overlay_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Base currency change
        base_currency_label = tk.Label(self.overlay_frame, text="Select Base Currency:")
        base_currency_label.pack()

        base_currency_var = tk.StringVar(self.overlay_frame)
        base_currency_var.set(self.data.get_status()[0])  # Default value
        base_currency_dropdown = tk.OptionMenu(self.overlay_frame, base_currency_var, "USD", "EUR", "JPY", "GBP")
        base_currency_dropdown.pack()

        # Select Currencies
        currency_label = tk.Label(self.overlay_frame, text="Select Currency:")
        currency_label.pack()

        currency_var = tk.StringVar(self.overlay_frame)
        currency_var.set("Select")  # Default value
        currency_dropdown = tk.OptionMenu(self.overlay_frame, currency_var, "USD", "KRW", "JPY", "GBP")
        currency_dropdown.pack()

        # Select Assets
        asset_label = tk.Label(self.overlay_frame, text="Select Asset:")
        asset_label.pack()

        asset_var = tk.StringVar(self.overlay_frame)
        asset_var.set("Select")  # Default value
        asset_dropdown = tk.OptionMenu(self.overlay_frame, asset_var, "GOLD", "SILVER", "COPPER", "CRUDE")
        asset_dropdown.pack()

        # Select securities
        security_label = tk.Label(self.overlay_frame, text="Select Security:")
        security_label.pack()

        security_var = tk.StringVar(self.overlay_frame)
        security_var.set("Select")  # Default value
        security_dropdown = tk.OptionMenu(self.overlay_frame, security_var, "BTC", "ETH", "DGC", "MNX")
        security_dropdown.pack()

        # Submit button within the overlay
        submit_button = tk.Button(self.overlay_frame, text="Submit", command=lambda: self.process_search(base_currency_var.get(), currency_var.get(), asset_var.get(), security_var.get()))
        submit_button.pack(pady=20)

    def process_search(self, new_base, selected_currencies, selected_assets, selected_securities):
        self.base = new_base

        self.overlay_frame.destroy()

    def start_data(self):

        initialData = self.data.return_basic()

        date = initialData[0]
        currencies = initialData[1]
        assets = initialData[2]
        securities = initialData[3]

        for i in range(0, len(currencies)):
            self.currencies.insert(INSERT, currencies[i] + '\n')

        for i in range(0, len(assets)):
            self.assets.insert(INSERT, assets[i] + '\n')

        for i in range(0, len(securities)):
            self.securities.insert(INSERT, securities[i] + '\n')

        self.date_label.config(text=date)



