import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("SVG")
@allure.description("Verify svg")
def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Mac Mini")
    
    list_of_svg = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    list_of_svg[0].click()

