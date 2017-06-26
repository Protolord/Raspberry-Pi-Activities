import ubidots

tokenValue = ""     # Place your token value here
variableId = ""     # Place your variable id here

print("Initializing")
api = ubidots.ApiClient(token = tokenValue)
testData = api.get_variable(variableId)

print("Retrieving values")
testDataValues = testData.get_values()

for i in range(len(testDataValues) - 1, -1, -1):
    print(testDataValues[i]['value'])
print("Done")


