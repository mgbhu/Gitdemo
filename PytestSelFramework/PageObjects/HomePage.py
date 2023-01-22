from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage



class Homepage:

    def __init__(self, driver):
        self.driver = driver
    shop = (By.LINK_TEXT, "Shop")

    def ShopItems(self):
       self.driver.find_element(*Homepage.shop).click()
       checkoutPage = CheckOutPage(self.driver)
       return checkoutPage