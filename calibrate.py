# this code will simply give user opportunity to set
# GPIO high and low to test light intensity

# below ascii art indicates pinout
# pins marked with xs are used in this code
#              Pin 1 Pin2
#           +3V3 [ ] [ ] +5V
# SDA1 / GPIO  2 [ ] [ ] +5V
# SCL1 / GPIO  3 [ ] [ ] GND
#        GPIO  4 [ ] [x] GPIO 14 / TXD0
#            GND [ ] [x] GPIO 15 / RXD0
#        GPIO 17 [ ] [x] GPIO 18
#        GPIO 27 [ ] [ ] GND
#        GPIO 22 [ ] [x] GPIO 23
#           +3V3 [ ] [x] GPIO 24
# MOSI / GPIO 10 [ ] [ ] GND
# MISO / GPIO  9 [ ] [x] GPIO 25
# SCLK / GPIO 11 [ ] [ ] GPIO  8 / CE0#
#            GND [ ] [ ] GPIO  7 / CE1#
#ID_SD / GPIO  0 [ ] [ ] GPIO  1 / ID_SC
#        GPIO  5 [ ] [ ] GND
#        GPIO  6 [ ] [ ] GPIO 12
#        GPIO 13 [ ] [ ] GND
# MISO / GPIO 19 [ ] [ ] GPIO 16 / CE2#
#        GPIO 26 [ ] [ ] GPIO 20 / MOSI
#            GND [ ] [ ] GPIO 21 / SCLK
#             Pin 39 Pin 40

import RPi.GPIO as GPIO

# set the pin numbering scheme
GPIO.setmode(GPIO.BCM)
#set all pins to output mode
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

high = False
print("Press enter to toggle GPIO lines")
while(1):
    x = input("")
    if (high == False):
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        print("GPIO lines set to high")
        high = True
    else:
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        print("GPIO lines set to low")
        high = False
