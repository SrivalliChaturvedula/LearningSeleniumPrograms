import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


@allure.title("Exception handle")
@allure.description("Exception handle")
def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    try:
        driver.find_element(By.ID, "This-value-not-exist")
    except NoSuchElementException as nse:
        print(nse.msg)
