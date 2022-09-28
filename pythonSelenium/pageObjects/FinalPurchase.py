import time

from selenium.webdriver.common.by import By


class FinalPurchase:
    def __init__(self, driver):
        self.driver = driver

    deliveryTextbox = (By.ID, "country")
    linkText = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def completePurchase(self, text):
        self.driver.find_element(*FinalPurchase.deliveryTextbox).send_keys(text)
        time.sleep(7)
        self.driver.find_element(*FinalPurchase.linkText).click()
        self.driver.find_element(*FinalPurchase.checkbox).click()
        self.driver.find_element(*FinalPurchase.purchaseButton).click()
        self.driver.find_element(*FinalPurchase.purchaseButton).click()
        successText = self.driver.find_element(*FinalPurchase.success).text
        assert "Success! Thank you!" in successText
        self.driver.get_screenshot_as_file("screen.png")