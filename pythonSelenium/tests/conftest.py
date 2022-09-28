import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# Running with Chrome instance command: py.test --browser_name chrome
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("C:\\Users\\khoam\\PycharmProjects1\\Driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service("C:\\Users\\khoam\\PycharmProjects1\\Driver\\gecko.exe")
        driver = webdriver.Firefox(service=s)
    elif browser_name == "IE":
        s = Service("C:\\Users\\khoam\\PycharmProjects1\\Driver\\ie.exe")
        driver = webdriver.Ie(service=s)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()