from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()

    # POST request to create a new fresh copy of Chrome
    # Fresh -Chrome - Session ID

    driver.get("https://app.vwo.com")
    # Code - HTTP Request - Chrome driver(Selenium Manager) -> Chrome(Session ID)

    print(driver.title)
    # GET Request

    assert driver.title == "Login - VWO"

