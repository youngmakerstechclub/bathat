from gpiozero import DistanceSensor
import gpiozero
import time                                             # Import time library

TRIG1 = 3                                               # Associate pin 23 to TRIG
ECHO1 = 14                                              # Associate pin 24 to ECHO
TRIG2 = 23
ECHO2 = 27
TRIG3 = 10
ECHO3 = 11
TRIG4 = 5
ECHO4 = 12
TRIG5 = 26
ECHO5 = 20

m1 = 15
m2 = 24
m3 = 18
m4 = 16
m5 = 25

maxdist = 1

try:
    print "[WAIT] Setup is now initializing the motorials."    
    mot1 = gpiozero.PWMLED(m1)
    mot2 = gpiozero.PWMLED(m2)
    mot3 = gpiozero.PWMLED(m3)
    mot4 = gpiozero.PWMLED(m4)
    mot5 = gpiozero.PWMLED(m5)

    print "[WAIT] Setup is now initializing the sensors."


    ultrasonic1 = DistanceSensor(echo=ECHO1, trigger=TRIG1, max_distance=maxdist)
    ultrasonic2 = DistanceSensor(echo=ECHO2, trigger=TRIG2, max_distance=maxdist)
    ultrasonic3 = DistanceSensor(echo=ECHO3, trigger=TRIG3, max_distance=maxdist)
    ultrasonic4 = DistanceSensor(echo=ECHO4, trigger=TRIG4, max_distance=maxdist)
    ultrasonic5 = DistanceSensor(echo=ECHO5, trigger=TRIG5, max_distance=maxdist)

    print("M1: " + str(ultrasonic1.distance))
    print("M2: " + str(ultrasonic2.distance))
    print("M3: " + str(ultrasonic3.distance))
    print("M4: " + str(ultrasonic4.distance))
    print("M5: " + str(ultrasonic5.distance))

    while True:
        mot1.value = 1 - ultrasonic1.distance
        mot2.value = 1 - ultrasonic2.distance
        mot3.value = 1 - ultrasonic3.distance
        mot4.value = 1 - ultrasonic4.distance
        mot5.value = 1 - ultrasonic5.distance

        time.sleep(0.1)
except KeyboardInterrupt:
    mot1.value = 0
    mot2.value = 0
    mot3.value = 0
    mot4.value = 0
    mot5.value = 0
