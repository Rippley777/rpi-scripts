from gpiozero import InputDevice
import time

# Define the pin connected to the DHT11's data
dht_pin = InputDevice(27)  # Replace 27 with your GPIO pin number

while True:
    if dht_pin.is_active:
        print("Sensor Active")
    else:
        print("No Signal")
    time.sleep(1)
