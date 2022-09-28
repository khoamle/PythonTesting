from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pythonSelenium.pageObjects.CheckOutPage import CheckOutPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def checkoutProduct(self, choice):
        products = self.driver.find_elements(*ShopPage.products)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == choice:
                product.find_element(By.XPATH, "div/button").click()
                actions = ActionChains(self.driver)
                actions.scroll_to_element(self.driver.find_element(*CheckOutPage.checkoutButton)).click().perform()
        return CheckOutPage(self.driver)