import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

@allure.title("Verify the values of rows and columns in table")
@allure.description("Verify Helen Benett is in which country by using Xpath Axes")
def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    table = driver.find_element(By.XPATH, "//table[@id='customers']")
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'customers')]/tbody/tr")
    row = len(row_elements)

    column_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'customers')]/tbody/tr[2]/td")
    column = len(column_elements)

    first_part = "//table[contains(@id, 'customers')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row+1):
        for j in range(1, column+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            # dynamic_link = driver.find_elements(By.XPATH, "//table[contains(@id, 'customers')]/tbody/tr[i]/td[j]")
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path)
                print(f"Helen Benett is in {country_text.text}")










