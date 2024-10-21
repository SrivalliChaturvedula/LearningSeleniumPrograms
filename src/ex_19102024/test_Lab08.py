import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Negative - login functionality")
@allure.description("Verify that if email/password is wrong we will get an error message")
def test_negative_vwo_login_verification():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    username = driver.find_element(By.ID, "login-username")
    username.send_keys("abc@gmail.com")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("12345")
    sign_in = driver.find_element(By.ID, "js-login-btn")
    sign_in.click()
    time.sleep(3)
    text_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    assert text_message.text == "Your email, password, IP address or location did not match"
    print(text_message.text)
