from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_open_vwo_login():
    driver = webdriver.Chrome()  # Create the session
    driver.get("https://app.vwo.com/#/login")  # Navigate to URL
    assert driver.title == "Login - VWO"
    assert driver.current_url == "https://app.vwo.com/#/login"
    page_source_data = driver.page_source
    assert "login" in page_source_data


def test_Chrome_options():
    # Incognito mode -> history is not stored
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    time.sleep(10)
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")

    assert True == False
