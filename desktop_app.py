from tkinter import *
from views.AccountSelector import AccountSelector
from views.AddAccount import AddAccount
from views.ClassView import ClassView
from views.GradeOverview import GradeOverview
from scripts import WebDriverUtils

routes = {
    1: AccountSelector,
    2: AddAccount,
    3: GradeOverview,
    4: ClassView,
}

def change_page(page, root):
    for widget in root.winfo_children():
        widget.destroy()
    # Display that route
    routes[page](root)


root = Tk()
change_page(1, root)
root.mainloop()