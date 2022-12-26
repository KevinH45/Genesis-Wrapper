from scripts.WebDriverUtils import get_grades
from tkinter import *
from tkinter import ttk

class GradeOverview:
    def __init__(self, root, **kwargs):
        self.username = kwargs["username"]
        self.password = kwargs["password"]

        grade_data = self.refresh_data()
        container = Frame(root)

        title_label = ttk.Label(container, text=f"Grade Overview for {self.username}")
        title_label.configure(font=("Roboto", 18, "bold"), foreground="#0455d8")
        title_label.pack(anchor="center")

        component_dict = {}
        for course, info in grade_data.items():
            meta = info["meta"]
            grade = info["grades"]
            component_dict[course] = [ttk.LabelFrame(container, text=course)]
            component_dict[course].append(ttk.Label(component_dict[course][0], text=f"""{meta[0]} ({meta[1]})"""))
            component_dict[course].append(ttk.Label(component_dict[course][0], text=f"""{grade[0]} ({grade[1]})"""))

            component_dict[course][0].pack_propagate(False)
            component_dict[course][0].configure(width=300, height=100)
            component_dict[course][0].pack(side="top", fill="x", expand=True, padx=20, pady=20)

            component_dict[course][1].pack(anchor="w", expand=True)
            component_dict[course][1].configure(font=("Roboto", 11, "bold"))

            component_dict[course][2].pack(side="left", anchor="w", expand=True)
            component_dict[course][2].configure(font=("Roboto", 18, "italic"))

        container.pack(expand=True)


    def refresh_data(self):
        grades = get_grades(self.username, self.password)
        return grades

    def refresh_page(self):
        self.root.change_page(3, self.username, self.password)


