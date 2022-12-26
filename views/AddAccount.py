from tkinter import *
from tkinter import ttk
from scripts.LocalInterface import add_update_user
from scripts.WebDriverUtils import get_grades
import sv_ttk

class AddAccount:
    def __init__(self, root):
        self.root = root
        container = Frame(root)
        title_label = ttk.Label(container, text="Add an account")
        title_label.configure(font=("Roboto", 18, "bold"), foreground="#0455d8")
        title_label.pack(anchor="center", padx=10, pady=10)

        username_frame = Frame(container)
        username_label = ttk.Label(username_frame, text="Enter email")
        username_label.configure(font=("Roboto", 10), foreground="#0455d8")
        username_label.pack(side="left", anchor="center", padx=10, pady=10)
        self.username_entry = ttk.Entry(username_frame)
        self.username_entry.pack(side="right", anchor="center")
        username_frame.pack(anchor="center")

        password_frame = Frame(container)
        password_label = ttk.Label(password_frame, text="Enter password")
        password_label.configure(font=("Roboto", 10), foreground="#0455d8")
        password_label.pack(side="left", anchor="center", padx=10, pady=10)
        self.password_entry = ttk.Entry(password_frame)
        self.password_entry.pack(side="right", anchor="center")
        password_frame.pack(anchor="center")

        submit_button = ttk.Button(container, text="Add user", command=self.store_user)
        submit_button.pack(anchor="center", pady=20)

        container.pack(expand=True)

    def store_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        add_update_user(username, password)

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.root.change_page(1)

