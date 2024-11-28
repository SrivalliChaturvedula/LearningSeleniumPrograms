import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.title("windows testing")
@allure.description("handling two windows")
def test_windows():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle
    print(parent_window)

    click_here = driver.find_element(By.LINK_TEXT, "Click Here")
    click_here.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle) # child
        if "New Window" in driver.page_source:
            print("Testcase passed")
            break

    time.sleep(10)
    driver.quit()
