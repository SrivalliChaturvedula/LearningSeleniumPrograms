import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException


driver = webdriver.Chrome()


def test_handle_alert(driver):
    try:
        # Wait for the alert to be present and switch to it
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_time = driver.switch_to.alert
        return alert_time
    except (UnexpectedAlertPresentException, NoAlertPresentException):
        return None


try:
    # Navigate to the desired webpage
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Locate the button that triggers the JavaScript confirmation alert
    js_confirm_alert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    js_confirm_alert.click()

    # Attempt to handle the alert
    alert = test_handle_alert(driver)

    if alert is not None:
        # Get the result text before accepting or dismissing the alert
        result_text = driver.find_element(By.CSS_SELECTOR, "#result").text

        # Check which button to click based on the result text
        if "Ok" in result_text:
            alert.accept()  # Click "Ok" on the alert
        else:
            alert.dismiss()  # Click "Cancel" on the alert

        # Wait for the result text to update
        WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CSS_SELECTOR, "#result").text != result_text)
        result_text = driver.find_element(By.CSS_SELECTOR, "#result").text  # Update the result text

        # Assertions
        assert result_text == "You clicked: Ok", f"Expected 'You clicked: Ok' but got {result_text}"

    else:
        print("No alert was present to handle.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up by closing the driver
    driver.quit()
