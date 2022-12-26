from tkinter import *
from tkinter import ttk
from scripts.LocalInterface import retrieve_json
from scripts.WebDriverUtils import get_grades
import sv_ttk

class AccountSelector:

    def __init__(self, root):
        self.loaded_data = retrieve_json()
        container = Frame(root)

        title_label = ttk.Label(container, text="Choose your account")
        title_label.configure(font=("Roboto", 18, "bold"), foreground="#0455d8")
        title_label.pack(anchor="center", padx=10, pady=10)

        self.select_button = ttk.Combobox(container, text="Select account", values=list(self.loaded_data.keys()))
        self.select_button.pack(anchor="center")

        submit_button = ttk.Button(container, text="Login", command=self.gui_login)
        submit_button.pack(anchor="center", padx=10, pady=10)

        container.pack(expand=True)
        sv_ttk.use_light_theme()

    def gui_login(self):
        try:
            grades = get_grades(self.select_button.get(), self.loaded_data[self.select_button.get()])
        except:
            exit()
