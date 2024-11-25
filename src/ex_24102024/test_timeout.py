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
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable())
        driver.refresh()

    except StaleElementReferenceException as se:
        print(se.msg)

    time.sleep(5)