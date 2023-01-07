#from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo = Servo(18, min_pulse_width=0.72/1000, max_pulse_width=2.52/1000, pin_factory=factory)
interval = 0.8


def upper(angle):
    servo.value = -abs(angle/100)
    

def lower(angle):
    servo.value = abs(angle/100)

if __name__ == '__main__':
    while (True):
        upper(10)
        sleep(interval)
        lower(10)
        sleep(interval)
