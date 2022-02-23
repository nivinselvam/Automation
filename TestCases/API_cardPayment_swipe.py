import json
import time
import requests
from Utilities import ExcelProcessor, DBProcessor as db, ServerConnectivityProcessor as server, APIProcessor as api, \
    portal_processor
from DataProvider import GlobalVariables
from PageFactory import Portal_login, portal_transactions_search
from Configuration import Config

workbook = ExcelProcessor.initializeWorkbook(GlobalVariables.APIdata_excelPath)
print("**************************Login API**************************")
url = ExcelProcessor.getAPIEnviURL(workbook, GlobalVariables.Environment) + ExcelProcessor.getAPIDetails(workbook,
                                                                                                         "Login",
                                                                                                         "URL")
header = json.loads(str(ExcelProcessor.getAPIDetails(workbook, "Login", "Header")).replace("'", '"'))
requestPayload = json.loads(ExcelProcessor.getAPIDetails(workbook, "Login", "RequestBody"))
print("--------------------------API Request-----------------------")
print(requestPayload)
responseData = requests.post(url, headers=header, data=json.dumps(requestPayload))
time.sleep(3)
print("--------------------------API Response-------------------------")
responsePayload = responseData.json()
print(responsePayload)
sessionKey = responsePayload["sessionKey"]
# ----------------------------API Validation---------------------------
apiValidations = ExcelProcessor.getAPIValidations(workbook, "Login")
api.validateAPI(responsePayload, apiValidations)
# ----------------------------------------------------------------------

print("*********************Card payment swipe API*********************")
url = ExcelProcessor.getAPIEnviURL(workbook, GlobalVariables.Environment) + ExcelProcessor.getAPIDetails(workbook,
                                                                                                         "Card Payment",
                                                                                                         "URL")
header = json.loads(str(ExcelProcessor.getAPIDetails(workbook, "Card Payment", "Header")).replace("'", '"'))
requestPayload = json.loads(ExcelProcessor.getAPIDetails(workbook, "Card Payment", "RequestBody"))
print("---------------------------API Request--------------------------")
print(requestPayload)
txnAmount = requestPayload['amount']
responseData = requests.post(url, headers=header, data=json.dumps(requestPayload))
time.sleep(3)
print("--------------------------API Response--------------------------")
responsePayload = responseData.json()
print(responsePayload)
txnID = responsePayload['txnId']
# ------------------------------API Validation------------------------------
apiValidations = ExcelProcessor.getAPIValidations(workbook, "Card Payment")
api.validateAPI(responsePayload, apiValidations)
# --------------------------------------------------------------------------

print("--------------------Connecting to Server/DB---------------------")
tunnel = server.connectToServer(GlobalVariables.Environment, GlobalVariables.port)
conn = db.connectDB(tunnel, 'ezedemo', 'abc123', 'ezetap_demo')
query = "SELECT amount, device_serial, external_ref from ezetap_demo.txn where id='" + txnID + "';"
queryResult = db.runQuery(conn, query)
print(queryResult)
db.closeDBConnect(conn)
server.closeServerConnectivity(tunnel)
# ------------------------------DB Validation------------------------------
dbValidations = ExcelProcessor.getDBValidations(workbook, "Card Payment")
db.dbValidation(queryResult, dbValidations)
# --------------------------------------------------------------------------

# -----------------------Portal Validation-----------------------
print("-------------------Logging into Portal-------------------")
driver = Config.initializeChromeDriver()
Config.openWebPage(driver, GlobalVariables.URL)
Portal_login.login_to_portal(driver, "7778886660", "a123456")

if(portal_transactions_search.navigate_to_txnSearch(driver)):
    txn_details = portal_transactions_search.get_transaction_details(driver, txnID)
    validations = ExcelProcessor.getPortalValidations(workbook,"Card Payment")
    portal_processor.portal_validation(txn_details, json.loads(validations))
else:
    print("Transactions table is not displayed.")

driver.close()

# --------------------------------------------------------------------------
# Sixth Step - Charge slip
