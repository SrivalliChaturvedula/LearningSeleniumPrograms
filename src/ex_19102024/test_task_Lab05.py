

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from src.ex_19102024.random_email_generator import generate_random_email


def test_register_account_page():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(5)

    # //input[@id="login-username"]

    # < input
    # type = "text"
    # name = "firstname"
    # value = ""
    # placeholder = "First Name"
    # id = "input-firstname"
    #
    # class ="form-control" >

    first_name = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    first_name.send_keys("Srivalli")
    last_name = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    last_name.send_keys("Chaturvedula")
    e_mail = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    e_mail.send_keys(generate_random_email(domain="example.com"))
    tele_phone = driver.find_element(By.XPATH, "//input[@placeholder='Telephone']")
    tele_phone.send_keys("1234567890")

    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("12345")
    password_confirm = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    password_confirm.send_keys("12345")

    subscribe_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='0']")
    subscribe_radio.click()

    check_box = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='1']")
    check_box.click()

    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    time.sleep(3)

    success_message = driver.find_element(By.TAG_NAME, "h1").text

    # success_message = driver.find_element(By.XPATH, "//div/h1").text
    print("Title of the Page is: ", driver.title)
    print("Text to be validated is: ", success_message)
    assert success_message.__eq__("Your Account Has Been Created!")

    time.sleep(5)

