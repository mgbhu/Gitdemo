from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class Baseclass:
    pass