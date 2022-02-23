from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Locators
txt_username_name = "username"
txt_password_name = "password"
btn_SignIn_name = "Submit"

wait = ""
#Page Activities
def login_to_portal(driver, username, password):
    wait = WebDriverWait(driver, 15)
    element = driver.find_element(By.NAME, txt_username_name)
    element.clear()
    element.send_keys(username)
    element = driver.find_element(By.NAME, txt_password_name)
    element.clear()
    element.send_keys(password)
    element = driver.find_element(By.NAME, btn_SignIn_name)
    element.click()
    element = driver.find_element(By.XPATH, "//div[@class='navbar navbar-inverse navbar-fixed-top']")
    wait.until(expected_conditions.visibility_of(element))




