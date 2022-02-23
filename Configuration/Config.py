from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from DataProvider import GlobalConstants

wait = ""

def initializeChromeDriver():
    driver = webdriver.Chrome(GlobalConstants.chromeDriverPath)
    return driver

def openWebPage(driver, URL):
    wait = WebDriverWait(driver, 15)
    driver.get(URL)
    driver.maximize_window()
    element = driver.find_element(By.NAME, "username")
    wait.until(expected_conditions.visibility_of(element))