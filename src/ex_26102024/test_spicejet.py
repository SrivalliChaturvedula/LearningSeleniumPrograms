import time
import selenium
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure


@allure.title("spicejet verification")
@allure.description("scenario verification in spice jet site")
def test_search_tab():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 2  # 1 = Allow, 2 = Block
    })

    driver = webdriver.Chrome(options)
    driver.maximize_window()
    driver.get("https://www.spicejet.com/")

    wait = WebDriverWait(driver, 10)

    try:
        from_search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='From']")))
        from_search_bar.click()

        actions = ActionChains(driver)
        actions.send_keys("DEL").perform()
        actions.send_keys(Keys.ENTER).perform()

        # Wait for the "To" field to be clickable
        to_search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='To']")))

        # Scroll the "To" field into view
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", to_search_bar)

        # Dismiss the blocking element if it's present
        try:
            # Locate the blocking element using the provided XPath
            blocking_element = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-b5h31w r-95jzfe']")
            if blocking_element.is_displayed():
                print("Blocking element found, hiding it.")
                # Use JavaScript to hide the blocking element
                driver.execute_script("arguments[0].style.display='none';", blocking_element)
        except Exception as e:
            print("No blocking element found or not displayed:", e)

        # Wait for any dynamic UI to stabilize, e.g., drop-downs, modals, etc.
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-b5h31w r-95jzfe']")))

        # Try clicking the "To" field after making sure it's visible and no elements block it
        try:
            actions2 = ActionChains(driver)
            actions2.move_to_element(to_search_bar).click().perform()
        except ElementClickInterceptedException:
            # Use JavaScript to click directly if the element is still blocked
            print("Click intercepted, using JavaScript executor")
            driver.execute_script("arguments[0].click();", to_search_bar)

        # Continue with sending "HYD" for the "To" field
        actions2 = ActionChains(driver)
        actions2.send_keys("HYD").perform()
        actions2.send_keys(Keys.ENTER).perform()

        # to_search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='To']")))
        # print("To field found in DOM:", to_search_bar.is_displayed())
        # driver.execute_script("arguments[0].scrollIntoView(true);", to_search_bar)
        # try:
        #     wait.until(EC.invisibility_of_element_located((By.XPATH, "//input[@class='css-1cwyjr8']")))
        #     print("Input field is no longer blocking.")
        # except Exception as e:
        #     print("Error waiting for input field:", e)
        #
        #
        # try:
        #     to_search_bar.click()
        # except ElementClickInterceptedException as e:
        #     print("CLick interception", e)
        #     driver.execute_script("arguments[0].click();", to_search_bar)
        #
        # actions2 = ActionChains(driver)
        # actions2.send_keys("HYD").perform()
        # actions2.send_keys(Keys.ENTER).perform()

        time.sleep(10)

        # departure_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Departure Date']")))
        # departure_date.click()

    finally:
        driver.quit()
