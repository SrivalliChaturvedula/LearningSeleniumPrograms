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

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options)
    driver.get("https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()

    main_window_handle = driver.current_window_handle

    list = driver.find_elements(By.CSS_SELECTOR, "[data-qa='yedexafobi']")
    # control  = 0
    # version = 1

    variation = list[1]
    action = ActionChains(driver=driver)
    action.click(variation).perform()

    time.sleep(15)

    all_handles = driver.window_handles  # 2
    print(all_handles)


    for handle in all_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.switch_to.frame("heatmap-iframe")
            click_map = driver.find_element(By.CSS_SELECTOR, "[data-qa='jitiqozozi']")
            click_map.click()
            time.sleep(10)







    time.sleep(5)
    driver.quit()

