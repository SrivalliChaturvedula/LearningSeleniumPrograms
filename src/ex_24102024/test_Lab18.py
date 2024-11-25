import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Drop down")
@allure.description("Verify Drop down")
def test_drop_down():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    select_button = driver.find_element(By.ID, "dropdown")
    select = Select(select_button)

    select.select_by_index(1)
    time.sleep(5)
