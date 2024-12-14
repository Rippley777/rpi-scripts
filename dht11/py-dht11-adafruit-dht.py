import Adafruit_DHT

# Define the sensor type and GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 13  # GPIO pin where the DATA pin is connected (e.g., GPIO4)

try:
    while True:
        # Read the temperature and humidity from the sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from sensor")
except KeyboardInterrupt:
    print("Exiting program")
