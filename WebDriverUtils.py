from extensions import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataExtractor import DataExtractor

def login(username, password):

    user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_username")))
    user.send_keys(username)
    pas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "j_password")))
    pas.send_keys(password)
    driver.find_element(By.CLASS_NAME, "saveButton").click()
    return True

def get_grades(username, password):
    driver.get("https://students.mtps.com/")
    driver.minimize_window()

    status = login(username, password)
    if status:
        driver.find_elements(By.CLASS_NAME, "headerCategoryTab")[3].click()
        dataExtractor = DataExtractor(driver.page_source)
        return dataExtractor.get_grade_data()
    return False
