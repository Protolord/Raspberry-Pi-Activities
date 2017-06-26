import ubidots

tokenValue = ""     # Place your token value here
variableId = ""     # Place your variable id here

print("Initializing")
api = ubidots.ApiClient(token = tokenValue)
testData = api.get_variable(variableId)

print("Uploading Data")
testData.save_value({"value": 40})
print("Done")
