import dht11
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Set up the sensor
sensor = dht11.DHT11(pin=27)  # Replace with your GPIO pin

while True:
    result = sensor.read()
    if result.is_valid():
        print(f"Temperature: {result.temperature}°C")
        print(f"Humidity: {result.humidity}%")
    else:
        print("Failed to read sensor data.")
    time.sleep(2)
