from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

service = Service(r"edgedriver_win64/msedgedriver.exe")
options = Options()
driver = webdriver.Edge(service=service, options=options)