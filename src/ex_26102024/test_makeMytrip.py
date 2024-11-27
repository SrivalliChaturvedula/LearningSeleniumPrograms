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


@allure.title("makemytrip verification")
@allure.description("scenario verification in makemytrip site")
def test_search_tab():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )
    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

    time.sleep(2)

    fromCity = driver.find_element(By.XPATH, "//input[@id='fromCity']")

    '''
    1. move to the fromCity
    2. click on it
    3. DEL Enter
    4. arrow down and enter
    '''

    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys_to_element(fromCity, "del")
     .perform())

    time.sleep(2)

    (actions.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())




    time.sleep(10)
