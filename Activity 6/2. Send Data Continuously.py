import ubidots
import random
import time

tokenValue = ""     # Place your token value here
variableId = ""     # Place your variable id here

try:
    print("Program initializing")
    api = ubidots.ApiClient(token = tokenValue)
    testData = api.get_variable(variableId)
    while True:
        randomValue = 100*random.random()
        print("Uploading Random Data: " + str(randomValue))
        testData.save_value({"value": randomValue})
        time.sleep(5)
        
except KeyboardInterrupt:
    print("Program terminating")

except:
    print("An unexpected error occurs")

    

