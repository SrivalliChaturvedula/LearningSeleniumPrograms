import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.title("Actions")
@allure.description("Verify actions.")
def test_verify_actions_keyboard_events():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    '''
    xpath : //input[@name='firstname']
    css: input[name='firstname']
    By.name = firstname
    '''

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # first_name.send_keys("testing")

    actions = ActionChains(driver=driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(first_name, "the testing academy")
     .key_up(Keys.SHIFT).perform()
     )


    time.sleep(5)
    driver.quit()


