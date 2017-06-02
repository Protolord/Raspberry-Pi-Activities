import RPi.GPIO as GPIO     # Import the General-purpose input/output library

GPIO.setmode(GPIO.BOARD)    # Set GPIO to use board numbering
GPIO.setup(7, GPIO.OUT)     # Set pin 7 as an output

# Use this command to turn on the LED
GPIO.output(7, 1)           # Make pin 7 output 3.3 V
# GPIO.output(7, True) also works

# Use this command to turn off the LED
# GPIO.output(7, 0)           # Make pin 7 output 0 V
# GPIO.output(7, False) also works
GPIO.cleanup(7)
