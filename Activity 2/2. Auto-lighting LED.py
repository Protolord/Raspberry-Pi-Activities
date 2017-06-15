import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
threshold = 50

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
        if counter >= threshold:
            GPIO.output(12, 1)
        else:
            GPIO.output(12, 0)

except:
    print("Program terminating")
    GPIO.cleanup(7)
    GPIO.cleanup(12)

