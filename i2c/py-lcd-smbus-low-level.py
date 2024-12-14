import smbus
from time import sleep

I2C_ADDR = 0x27
bus = smbus.SMBus(1)

# Initialize LCD
bus.write_byte_data(I2C_ADDR, 0x00, 0x38)  # Function set
bus.write_byte_data(I2C_ADDR, 0x00, 0x0C)  # Display on, cursor off
bus.write_byte_data(I2C_ADDR, 0x00, 0x01)  # Clear display
sleep(0.1)

# Send "Hello"
for char in "Hello":
    bus.write_byte_data(I2C_ADDR, 0x40, ord(char))
