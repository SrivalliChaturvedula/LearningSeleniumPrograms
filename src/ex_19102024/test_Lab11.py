import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Finding all the buttons")
def test_button_using_tag_name():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))
    for i in buttons:
        print(i.text)

    all_links_in_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_in_page))

    for j in all_links_in_page:
        print(j.text)

    time.sleep(5)
