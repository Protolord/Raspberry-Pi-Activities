import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT)

blink = True
blinkCounter = 0
prevState = True
newState = True

# Mode 1: Blinking LED
# Mode 2: Steady ON LED
# Mode 3: Steady OFF LED
mode = 1 # Start the program in mode 1

try:
    print("Press the button to change the lighting activity of the LED")
    print("Now in mode 1")
    while True:
        # LED lighting based on current mode
        if mode == 1:
            GPIO.output(7, blink)
            blinkCounter += 1
            if blinkCounter > 10:
                blink = not blink    # Invert the value of blink
                blinkCounter = 0
        elif mode == 2:
            GPIO.output(7, 1)
        elif mode == 3:
            GPIO.output(7, 0)

        # Detect button push
        # GPIO.input(11) is false when button is pressed
        newState = GPIO.input(11)
        if prevState != newState:
            if not newState:
                mode += 1
                if mode > 3:
                    mode = 1
                    blink = True
                    blinkCounter = 0
                print("Button pressed, now in mode", mode)
                # Pause program while push button is in bouncing state
                time.sleep(0.2) 
            prevState = newState
        time.sleep(0.05)

except:
    print("Program terminating")
    GPIO.cleanup(7)
    
    
    
    
