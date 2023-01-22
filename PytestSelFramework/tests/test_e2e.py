from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import Homepage
from utilities.BaseClass import Baseclass





class Test(Baseclass):

     def test_e2e(self):
          homepage = Homepage(self. driver)
          checkOutPage = homepage.ShopItems()
          # checkoutPage = CheckOutPage(self.driver)
          products = checkOutPage.getProductTitles()

          # print product names

          #products = self.driver.find_elements(By.XPATH, "//h4[@class='card-title']/a")
          i = -1
          for prod in products:
               i = i + 1
               print(prod.text)
               # add balckberry to cart
               if ('Blackberry' == prod.text):
                    checkOutPage.getProductFooter()[i].click()

          # ch3ckout

          self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
          self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
          textbox = self.driver.find_element(By.ID, "country")
          textbox.send_keys("ind")
          wait = WebDriverWait(self.driver, 15)
          wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
          countryName = self.driver.find_element(By.LINK_TEXT, "India")
          countryName.click()

          ##CHECKBOX

          self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
          ##PURCHASE
          self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

          SuccessMsg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
          print(SuccessMsg.text)

          # driver.close()








