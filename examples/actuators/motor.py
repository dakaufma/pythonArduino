import sys
sys.path.append("../..")
import time

import arduino

ard = arduino.Arduino()
m0 = arduino.Stepper(ard, 5, 6)
ard.run()  # Start the Arduino communication thread

while True:
    m0.step(100)
    print "step"
    time.sleep(1)
    m0.step(100)
    time.sleep(1)
    m0.step(100)
    time.sleep(1)
    m0.step(100)
    time.sleep(1)
