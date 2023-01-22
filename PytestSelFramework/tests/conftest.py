
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope='class')
def setup(request):
        browser_name = request.config.getoption("browser_name")
        if browser_name == 'firefox':
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            driver = webdriver.Firefox(executable_path=r'F:\geckodriver.exe', options=options)
            # driver = webdriver.Firefox()
        elif browser_name == "chrome":

            driver = webdriver.Chrome(executable_path=r'C:\Users\Monika\PycharmProjects')

        driver.get('https://rahulshettyacademy.com/angularpractice/')
        driver.maximize_window()

        request.cls.driver = driver
        yield
