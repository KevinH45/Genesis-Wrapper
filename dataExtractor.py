# MASSIVE credit to Zenesus: https://github.com/Zenesus/Zenesus-backend/blob/main/scripts/data.py
# Though the data is structured a bit differently, Zenesus was VERY VERY helpful in getting started

from bs4 import BeautifulSoup


class DataExtractor(BeautifulSoup):

    def __init__(self, html, **kwargs):
        super().__init__(html, features="html.parser", **kwargs)
        self.html = html
        self.parser = "html.parser"

    def _extract_meta(self, meta):

        email = str(meta.find("a")["href"]).replace("mailto:", "").replace("\n","").strip()
        name = str(meta.text).replace("Email:", "").replace("\n", "").strip()
        return [name, email]


    def _extract_grades(self, grades):
        grade_data = grades.find("table").find("tr").find_all("td")
        percent = grade_data[0].find("div").text.replace("\n", "").strip()
        letter_grade = grade_data[1].text.replace("\n", "").strip()

        return [percent, letter_grade]

    def get_grade_data(self):
        # {"COURSE": {"meta":["Teacher Name", "Email", "Followup Link"], "grades":[100.0%, "A+"]}}

        course_data = {}

        outer_table = self.find("table", role="main")
        outer_row = outer_table.find_all("tr")[1] # Extract second row (first row is useless junk)
        inner_table = outer_row.find("table", class_="list").find("tbody")
        row_even = inner_table.find_all("tr", class_="listroweven", recursive=False) # only extract direct children
        row_odd = inner_table.find_all("tr", class_="listrowodd", recursive=False) # only extract direct children
        rows = row_even + row_odd

        for row in rows:
            course = row.find_all("td", class_="cellLeft")[0].find("span").find("u").text.replace("\n", "").strip()
            meta = self._extract_meta(row.find_all("td", class_="cellLeft", recursive=False)[1])
            grades = self._extract_grades(row.find_all("td", class_="cellRight", recursive=False)[0])

            course_data[course] = {"meta": meta, "grades": grades}

        return course_data



