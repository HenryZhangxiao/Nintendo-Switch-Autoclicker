This servo controller uses PiGPIO to modulate the pulses. Upon the first time running you must start the PiGPIO server with `sudo pigpiod`

Using PiGPIO allows us to send hardware generated pulses. If you don't use the pigpio subsystem you may find that there is a lot of jitter and your servo doesn't/can't interpret the pulses correctly.
If you know that software modulation works, you can use that instead.

The fastest time between keypresses was 0.30019092559814453 seconds
The slowest time between keypresses was 45.38012194633484 seconds
The average time between keypresses was 7.4502109902576334 seconds