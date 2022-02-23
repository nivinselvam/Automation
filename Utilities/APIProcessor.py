import json
from prettytable import PrettyTable
from Utilities import ExcelProcessor
from DataProvider import GlobalVariables

custTable = PrettyTable(["Field", "Expected Value", "Actual Value", "Status"])

def validateAPI(responsePayload, apiValidations):
    apiValidations = json.loads(apiValidations.replace("'", '"'))
    print("--------------------API validation--------------------")
    for key in apiValidations:
        try:
            if apiValidations[key] == str(responsePayload[key]):
                # print("Passed : Expected value '"+apiValidations[key]+"' for field '"+key+"' is correct in the response packet")
                custTable.add_row([key, apiValidations[key], str(responsePayload[key]), "Passed"])
            else:
                # print("Failed : Expected value '"+apiValidations[key]+"' for field is '"+key+"' but received value is '"+str(responsePayload[key])+"'")
                custTable.add_row([key, apiValidations[key], str(responsePayload[key]), "Failed"])
        except KeyError:
            print("Failed : Expected Field '"+key+"' is not available in the response packet")
    print(custTable)
