import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.title("Testcase to verify text of rows and cols")
@allure.description("Verify whether Dubai is present in the columns of the table or not")
def test_dynamic_web_table():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    # row_table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody/tr")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            if "Dubai" in e.text:
                print("YES")
                break


