from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def test_windows():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options)
    driver.get(
        "https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()

    try:
        # Get the main window handle
        main_window_handle = driver.current_window_handle

        # Wait for the elements to appear on the page
        wait = WebDriverWait(driver, 15)
        list_windows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-qa='voferojeve']")))

        # Validate that the list has at least two elements
        if len(list_windows) > 1:
            # Click the second element (variation)
            variation = list_windows[1]
            print("Element found:", variation)

            # Perform the click action
            action = ActionChains(driver)
            action.move_to_element(variation).click().perform()
        else:
            print("Not enough elements found in the list to perform the desired action.")

    except NoSuchElementException:
        print("The specified elements were not found on the page.")
    except TimeoutException:
        print("Timed out waiting for the elements to load.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Optional: Close the browser
        time.sleep(5)  # To observe the result before quitting
        driver.quit()


# Run the test
test_windows()
