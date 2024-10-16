from selenium import webdriver

def test_sample1():
    driver = webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"