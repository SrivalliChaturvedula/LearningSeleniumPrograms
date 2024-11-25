import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.title("Actions p2")
@allure.description("Verify mouse actions.")
def test_verify_actions_mouse_events():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    click_link = driver.find_element(By.ID, "click")
    click_link.click()

    time.sleep(2)

    action_builder = ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()




    time.sleep(10)
    driver.quit()

