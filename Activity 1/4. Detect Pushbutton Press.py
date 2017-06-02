import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
prevState = False
newState = False

try:
    print("Program starting")
    while True:
        newState = GPIO.input(11)
        # When the current state of GPIO input is not the same as the previous
        # recorded state
        if prevState != newState:
            if newState:
                print("Button pressed")
                # Pause program while push button is in bouncing state
                time.sleep(0.2) 
            prevState = newState
                
except:
    print("Program terminating")

    
