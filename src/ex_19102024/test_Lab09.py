import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@allure.title("Positive - Start a free trial link verification")
@allure.description("When clicked on Start a free trial new page has to be loaded.")
def test_link():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # LINK_TEXT = EXACT Text
    anchor_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"


    driver.back()