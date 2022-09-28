from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\khoam\\PycharmProjects1\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("https://google.com")
driver.close()
driver.quit()