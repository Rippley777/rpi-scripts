import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(17, GPIO.OUT)  # Set GPIO17 as an output pin

# Blink LED
try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn LED on
        time.sleep(1)              # Wait 1 second
        GPIO.output(17, GPIO.LOW)  # Turn LED off
        time.sleep(1)              # Wait 1 second
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Reset GPIO settings
