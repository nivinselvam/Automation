import json
import pymysql
import pandas
from prettytable import PrettyTable
from Utilities import ExcelProcessor

custTable = PrettyTable(["Field", "Expected Value", "Actual Value", "Status"])

def connectDB(tunnel, username, password, database):
    conn = pymysql.connect(host='localhost', user=username, passwd=password, database=database,
                           port=tunnel.local_bind_port)
    return conn

def runQuery(conn, query):
    queryResult = pandas.read_sql_query(query, conn)
    return queryResult

def dbValidation(queryResult, dbValidations):
    result = queryResult.to_dict()
    dbValidations = json.loads(dbValidations.replace("'", '"'))
    print("--------------------DB validation--------------------")
    for key in dbValidations:
        expectedValue = dbValidations[key]
        actualValue = str((result[key])[0])
        try:
            if expectedValue == actualValue:
                # print("Passed : Expected value '" +expectedValue+ "' for field '" + key + "' is correct in the response packet")
                custTable.add_row([key, expectedValue, actualValue, "Passed"])
            else:
                # print("Failed : Expected value '" +expectedValue+ "' for field is '" + key + "' but received value is '" +actualValue+ "'")
                custTable.add_row([key, expectedValue, actualValue, "Failed"])
        except KeyError:
            print("Failed : Expected Field '" + key + "' is not available in the response packet")
    print(custTable)


def closeDBConnect(connection):
    connection.close()
