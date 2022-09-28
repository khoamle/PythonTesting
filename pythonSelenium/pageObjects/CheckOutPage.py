from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def clickCheckout(self):
        self.driver.find_element(*CheckOutPage.checkoutButton).click()
        return ConfirmationPage(self.driver)