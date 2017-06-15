import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100)
pwm.start(0)     # Initially start at 0% Duty Cycle

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
        pwm.ChangeDutyCycle(counter)

except:
    print("Program terminating")
    pwm.stop()
    GPIO.cleanup(7)
    GPIO.cleanup(12)

