from pythonSelenium.pageObjects.HomePage import HomePage
from pythonSelenium.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup):
        homePage = HomePage(self.driver)
        shopPage = homePage.clickShopButton()
        checkoutPage = shopPage.checkoutProduct("Blackberry")
        confirmationPage = checkoutPage.clickCheckout()
        finalPurchasePage = confirmationPage.clickCheckout()
        finalPurchasePage.completePurchase("ind")
