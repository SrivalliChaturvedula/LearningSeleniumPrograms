from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_chrome_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # find element in anchor tag

    # < a
    # id =
    # href = "./profile.php#login"
    #
    # class ="btn btn-dark btn-lg" > Make Appointment < / a >
    # we need to find unique attribute
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # click on it
    make_appointment_element.click()
    # verify URL Change
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
