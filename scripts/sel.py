from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from scripts.DataExtractor import DataExtractor


service = Service(r"../edgedriver_win64/msedgedriver.exe")
options = Options()
driver = webdriver.Edge(service=service, options=options)
driver.get("https://students.mtps.com/")
driver.minimize_window()

user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_username")))
user.send_keys("")
pas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_password")))
pas.send_keys("")
driver.find_element(By.CLASS_NAME, "saveButton").click()

driver.find_elements(By.CLASS_NAME, "headerCategoryTab")[3].click()
dataExtractor = DataExtractor(driver.page_source)

driver.find_elements(By.CLASS_NAME, "")
print(dataExtractor.get_grade_data())
