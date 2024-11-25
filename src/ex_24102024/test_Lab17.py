import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("Verify JS-Prompt Alerts")
def test_js_confirm_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_prompt_alert = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_prompt_alert.click()

    WebDriverWait(driver=driver, timeout=20).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    # alert.send_keys("Srivalli")
    # alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.CSS_SELECTOR, "#result").text

    # assert result_text == "You entered: Srivalli"

    assert result_text == "You entered: null"

    time.sleep(10)


