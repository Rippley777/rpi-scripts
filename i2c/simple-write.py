from RPLCD.i2c import CharLCD

# Replace 0x27 with your LCD's I2C address
lcd = CharLCD('PCF8574', 0x27)

# Write text to the LCD
lcd.write_string("Hello, I2C LCD!")

# Clear the LCD after 5 seconds
import time
time.sleep(5)
lcd.clear()
