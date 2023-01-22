from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//h4[@class='card-title']/a")
    productFooter = (By.XPATH, "//button[@class='btn btn-info']")
    checkoutPage = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.productTitle)

    def getProductFooter(self):
        return self.driver.find_elements(*CheckOutPage.productFooter)

    def getcheckoutPage(self):
        return self.driver.find_element(*CheckOutPage.checkoutPage)