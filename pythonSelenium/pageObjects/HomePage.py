from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopButton = (By.CSS_SELECTOR, "a[href*='shop']")

    def clickShopButton(self):
        self.driver.find_element(*HomePage.shopButton).click()
        return ShopPage(self.driver)
