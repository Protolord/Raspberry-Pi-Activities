import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

try:
    while True:
        counter = 0
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, 0)
        time.sleep(0.1)
        GPIO.setup(7, GPIO.IN)
        while not GPIO.input(7) and counter < 100:
            counter += 1
            time.sleep(0.01)
        print("Counter = ", counter)

except:
    print("Program terminating")
    GPIO.cleanup(7)

