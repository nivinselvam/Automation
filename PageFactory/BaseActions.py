from selenium.webdriver.common.by import By

def enter_data(driver, locator, value):
    if str(locator).endswith("_NAME"):
        element= driver.find_element(By.NAME, locator)
        element.clear()
        element.send_keys(value)
    elif str(locator).endswith("_XPATH"):
        element = driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(value)
    elif str(locator).endswith("_ID"):
        element = driver.find_element(By.ID, locator)
        element.clear()
        element.send_keys(value)


def click(driver, locator):
    if str(locator).endswith("_NAME"):
        driver.find_element(By.NAME, locator).click()


    elif str(locator).endswith("_XPATH"):
        driver.find_element(By.XPATH, locator).click()

    elif str(locator).endswith("_CLASS"):
        driver.find_element(By.CLASS_NAME, locator).click()

    elif str(locator).endswith("_ID"):
        driver.find_element(By.ID, locator).click()


# def click_specific(driver, locator, value):
#     if str(locator).endswith("_NAME"):
#         element = driver.find_element(By.NAME, configReader.read_conf_with_spec_val("locators", locator, value))
#         element.click()
#
#     elif str(locator).endswith("_XPATH"):
#         element = driver.find_element(By.XPATH, configReader.read_conf_with_spec_val("locators", locator, value))
#         element.click()


# def press_enter_key(driver, locator):
#     if str(locator).endswith("_NAME"):
#         driver.find_element(By.NAME, locator).send_keys(Keys.ENTER)
#     elif str(locator).endswith("_XPATH"):
#         driver.find_element(By.XPATH, locator).send_keys(Keys.ENTER)
