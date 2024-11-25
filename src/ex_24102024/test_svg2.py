import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG2")
@allure.description("Verify svg2")
def test_svg2():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    # list_of_states = driver.find_elements(By.XPATH,
    #                                       "//*[name()='svg']//*[name()='g'][7]//*[name()='g']//*[name()='g']//*[name()='path']")

    try:
        # Wait for the SVG map to load
        list_of_states = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[name()='svg']//*[name()='g'][7]//*[name()='g']//*[name()='g']//*[name()='path']"))
        )

        for state in list_of_states:
            aria_label = state.get_attribute("aria-label")
            print(aria_label)
            if "Tripura" in aria_label:
                try:
                    state.click()
                except ElementClickInterceptedException:
                    # Fallback to JavaScript click if the regular click is intercepted
                    driver.execute_script("arguments[0].click();", state)
                break

    except NoSuchElementException:
        print("The SVG map or specified state could not be found.")

        # Wait briefly to observe the clicked result (or replace with further actions/assertions)
    time.sleep(5)
    driver.quit()


# Call the test function
test_svg2()
