from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.FinalPurchase import FinalPurchase


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutButton = (By.XPATH, "//button[@class='btn btn-success']")
    def clickCheckout(self):
        self.driver.find_element(*ConfirmationPage.checkoutButton).click()
        return FinalPurchase(self.driver)
