import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@allure.title("Exception handle")
@allure.description("Exception handle")
def test_stale_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        textarea.send_keys("Testing Acadmey")
    except StaleElementReferenceException as se:
        print(se.msg)

    time.sleep(5)
