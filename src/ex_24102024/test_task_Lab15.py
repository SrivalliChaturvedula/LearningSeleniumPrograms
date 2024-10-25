import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_radio_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    gender_button = driver.find_element(By.XPATH, "//input[@id='sex-1']")
    gender_button.click()

    automation_tester_checkbox = driver.find_element(By.XPATH, '//input[@id="profession-1"]')
    automation_tester_checkbox.click()

    years_of_exp_button = driver.find_element(By.XPATH, "//input[@id='exp-2']")
    years_of_exp_button.click()

    time.sleep(10)
    driver.quit()
