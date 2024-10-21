import time

from selenium import webdriver


def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"


def test_edge_current_url_verification():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"


def test_firefox_current_url_verification():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"
