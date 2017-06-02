import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
out = True

try:
    print("Program starting")
    while True:
        GPIO.output(7, out)
        out = not out
        time.sleep(0.5)
except:
    print("Program terminating")
    GPIO.cleanup(7)

    
