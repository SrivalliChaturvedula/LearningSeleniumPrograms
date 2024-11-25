import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.title("Click and hold Actions")
@allure.description("Verify click and hold actions.")
def test_verify_actions_keyboard_events():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    element_to_hold = driver.find_element(By.ID, "draggable")
    '''
    click is normal driver will find the element and click it.
    click and hold: using action class
    
    '''

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(5)

    drop_element = driver.find_element(By.ID, "droppable")

    actions.drag_and_drop(element_to_hold, drop_element).perform()

    status_text = driver.find_element(By.ID, "drop-status")
    assert status_text.text == "dropped"



    time.sleep(10)

