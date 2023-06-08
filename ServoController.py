#from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import sys
factory = PiGPIOFactory()

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo = Servo(18, min_pulse_width=0.72/1000, max_pulse_width=2.52/1000, pin_factory=factory)
UPPER_ANGLE = 10
LOWER_ANGLE = 10
INTERVAL = 0.8

def upper(angle):
    servo.value = -abs(angle/100)

def lower(angle):
    servo.value = abs(angle/100)

def calibrate():
    servo.min()
    sleep(5)
    servo.max()
    sleep(5)
    servo.mid()

if __name__ == '__main__':
    if sys.argv[1].lower() == 'calibrate' or sys.argv[1].lower() == 'c':
        calibrate()
    else:
        while (True):
            upper(UPPER_ANGLE)
            sleep(INTERVAL)
            lower(LOWER_ANGLE)
            sleep(INTERVAL)
