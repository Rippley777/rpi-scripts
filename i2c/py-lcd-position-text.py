import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()


mylcd.lcd_display_string("I LOVE SAM!!!!", 2, 3)
