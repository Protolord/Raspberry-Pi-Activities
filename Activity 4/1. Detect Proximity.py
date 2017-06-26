import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
prevState = False
newState = False
try:
    print("Program starting")
    while True:
        newState = GPIO.input(7)
        if prevState != newState:
            prevState = newState
            if newState:
                print("Nearby object detected")
            else:
                print("Nearby object gone")
        
except:
    print("Program terminating")

    
