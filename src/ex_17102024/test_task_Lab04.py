from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_change_url():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(5)
    button = driver.find_element(By.ID, "btn-make-appointment")
    button.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    button = driver.find_element(By.ID, "btn-login")
    button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
