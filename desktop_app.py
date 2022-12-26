from tkinter import *
from views.AccountSelector import AccountSelector
from views.AddAccount import AddAccount
from views.ClassView import ClassView
from views.GradeOverview import GradeOverview
from scripts import WebDriverUtils
import sv_ttk

class CustomTk(Tk):
    def change_page(self, page, **kwargs):
        routes = {
            1: AccountSelector,
            2: AddAccount,
            3: GradeOverview,
            4: ClassView,
        }

        for widget in self.winfo_children():
            widget.destroy()
        # Display that route
        routes[page](self, **kwargs)

root = CustomTk()
sv_ttk.use_light_theme()

root.change_page(1)
root.mainloop()
