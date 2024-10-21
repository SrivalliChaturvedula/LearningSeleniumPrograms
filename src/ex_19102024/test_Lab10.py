import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@allure.description("verifying free trial link using partial_text")
def test_link_using_partial_text():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # Partial link text
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
