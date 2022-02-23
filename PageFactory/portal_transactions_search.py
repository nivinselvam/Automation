from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Locators
tbl_txns_xpath = "//table[@id='table_txns']"
tbl_txnsHeader_xpath = "//table[@id='table_txns']/thead"
tbl_txnsBody_xpath = "//table[@id='table_txns']/tbody"
tbl_txnsRows_xpath = "//table[@id='table_txns']/tbody/tr"
tbl_txnsCols_xpath = "//table[@id='table_txns']/thead//th"
ddl_transaction_xpath = "//a[text()='Transactions ']"
mnu_transactionSearch_xpath = "//a[text()='Search']"

wait = ""

def navigate_to_txnSearch(driver):
    wait = WebDriverWait(driver, 15)
    element = driver.find_element(By.XPATH, ddl_transaction_xpath)
    element.click()
    element = driver.find_element(By.XPATH, mnu_transactionSearch_xpath)
    element.click()
    element = driver.find_element(By.ID, "searchform")
    wait.until(expected_conditions.visibility_of(element))
    element = driver.find_element(By.ID, "table_txns")
    if (expected_conditions.visibility_of(element)):
        print("Passed : Navigated to Transactions search page successfully.")
        return True
    else:
        print("Failed : Navigation to Transactions search page failed.")
        return False


def get_transaction_details(driver , txn_id):
    transactionRow = ""
    rowID = "ENT"+txn_id
    transactionDetails = {}
    total_transactions_count = len(driver.find_elements(By.XPATH, tbl_txnsRows_xpath))
    total_attributes_count = len(driver.find_elements(By.XPATH, tbl_txnsCols_xpath))

    for row in range(1, total_transactions_count+1):
        element = driver.find_element(By.XPATH, tbl_txnsRows_xpath + "[" + str(row) + "]")
        if element.get_attribute("id") == rowID:
            transactionRow = row
            break
    for col in range(1, total_attributes_count):
        attribute = driver.find_element(By.XPATH, tbl_txnsCols_xpath + "[" + str(col) + "]").get_attribute("aria-label")
        if attribute.__contains__(": activate to sort column ascending"):
            attribute = attribute.replace(": activate to sort column ascending","")
        attributeValue = driver.find_element(By.XPATH, tbl_txnsRows_xpath + "[" + str(transactionRow) + "]/td[" + str(col) + "]").text
        transactionDetails[attribute] = attributeValue
    return transactionDetails


