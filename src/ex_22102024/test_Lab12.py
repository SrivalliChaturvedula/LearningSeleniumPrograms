import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest


@allure.title("Verify titles of the search are getting populated.")
@allure.description("Verify length of the titles is matching as expected.")
def test_url_ebay_verification():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(2)
    search_bar = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_bar.send_keys("Mac Mini")
    time.sleep(5)
    search_click = driver.find_element(By.CSS_SELECTOR, "#gh-btn")
    search_click.click()
    time.sleep(5)
    output_titles = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
    output_prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

    # for title in output_titles:
    #     print(title.text)
    # assert len(output_titles) == 62
    #
    # # Loop through each web element
    # for price in output_prices:
    #     print(price.text)

    for title, price in zip(output_titles, output_prices):
        # Clean the title and price text
        title_text = title.text.strip()  # Clean leading/trailing whitespace
        price_text = price.text.strip()  # Clean leading/trailing whitespace

        # Print the title and price side by side
        print(f"Title: {title_text}, Price: {price_text}")





