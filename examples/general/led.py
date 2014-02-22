import sys
sys.path.append("../..")
import time

import arduino

ard = arduino.Arduino()
led = arduino.DigitalOutput(ard, 13)
ard.run() # Start the thread which communicates with the Arduino

def strum():
	pass

def fret():
	pass
# Make the LED blink once a second
while True:
    led.setValue(1)
    time.sleep(0.01)
    led.setValue(0)
    time.sleep(0.01)
