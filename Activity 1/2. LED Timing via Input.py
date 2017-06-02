import RPi.GPIO as GPIO     # Import the General-purpose input/output library
import time                 # Import timing library

GPIO.setmode(GPIO.BOARD)    # Set GPIO to use board numbering
GPIO.setup(7, GPIO.OUT)     # Set pin 7 as an output

# input() prompts the user to enter an input
waitTime = input("How long will the LED be turned on in second(s)? ")
GPIO.output(7, 1)           # Turns on the LED
time.sleep(float(waitTime)) # Wait
GPIO.output(7, 0)           # Turns off the LED
GPIO.cleanup(7)             # Remove the setup in pin 7 since we're done



