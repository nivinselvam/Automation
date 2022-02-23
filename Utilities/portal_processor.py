from prettytable import PrettyTable

custTable = PrettyTable(["Field", "Expected Value", "Actual Value", "Status"])

def portal_validation(portalValuesJSON, portalValidations):
    print("--------------------Portal validation--------------------")
    for key in portalValidations:
        if portalValidations[key] == str(portalValuesJSON[key]):
            # print("Passed : Expected value '" +portalValidations[key]+ "' for field '" + key + "' is correct in the response packet")
            custTable.add_row([key, portalValidations[key], str(portalValuesJSON[key]), "Passed"])
        else:
            # print("Failed : Expected value '" + portalValidations[key] + "' for field is '" + key + "' but received value is '" +str(portalValuesJSON[key])+ "'")
            custTable.add_row([key, portalValidations[key], str(portalValuesJSON[key]), "Failed"])
    print(custTable)
