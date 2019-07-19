

##traffic_light

from gpiozero import LED
from time import sleep

red = LED(27)
yellow = LED(17)
green = LED(4)
while True:
    
    green.on()
    sleep(2)
    green.off()  


    yellow.on()
    sleep(2)
    yellow.off()
    
    red.on()
    sleep(2)
    red.off()

    
   