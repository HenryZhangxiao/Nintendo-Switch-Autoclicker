#from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import sys
factory = PiGPIOFactory()

UPPER_ANGLE = 0
LOWER_ANGLE = 18
INTERVAL = 8
GPIO_DATA_PIN = 18

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo = Servo(GPIO_DATA_PIN, min_pulse_width=0.72/1000, max_pulse_width=2.52/1000, pin_factory=factory)
def upper(angle):
    servo.value = -abs(angle/100)

def lower(angle):
    servo.value = abs(angle/100)

def calibrate():
    sleep(3)
    servo.min()
    sleep(3)
    servo.max()
    sleep(3)
    servo.mid()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1].lower() == 'calibrate' or sys.argv[1].lower() == 'c':
            calibrate()
    else:
        while (True):
            upper(UPPER_ANGLE)
            sleep(INTERVAL)
            lower(LOWER_ANGLE)
            sleep(0.2)
