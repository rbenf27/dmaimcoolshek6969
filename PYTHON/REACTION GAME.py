

import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)
seconds = int(input(" How many seconds do you want the light to wait to turn on type here:"))
time.sleep(seconds)
GPIO.output(17, True)
while True:
    if GPIO.input(4) == 1:
        GPIO.output(17, False)
        print(" USER 1 WINS!!!!")
        break
    if GPIO.input(27) == 1:
        GPIO.output(17, False)
        print(" USER 2 WINS!!!!")
        break
    
GPIO.cleanup()
    
    


