# main code for light stimulatio project

# below ascii art indicates pinout
# pins marked with A-F indicate the column they control
#              Pin 1 Pin2
#           +3V3 [ ] [ ] +5V
# SDA1 / GPIO  2 [ ] [ ] +5V
# SCL1 / GPIO  3 [ ] [ ] GND
#        GPIO  4 [ ] [A] GPIO 14 / TXD0
#            GND [ ] [B] GPIO 15 / RXD0
#        GPIO 17 [ ] [C] GPIO 18
#        GPIO 27 [ ] [ ] GND
#        GPIO 22 [ ] [D] GPIO 23
#           +3V3 [ ] [E] GPIO 24
# MOSI / GPIO 10 [ ] [ ] GND
# MISO / GPIO  9 [ ] [F] GPIO 25
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
GPIO.setmode(BCM)
#set all pins to output mode
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def columnSet(column):
    #todo: write a function that takes user column input and
    # sets up frequency and duty cycle
    x = 0 #placeholder code

def runPWM():
    # todo: write function that starts PWM for all desired columns
    x = 0


while(1):
    print("Welcome to the Light Stimulation set up process!\n")
    print("Below is a visual representation of the LED array.\n ")
    print("Please select a column you would like to program.\n")
    print("|-----|-----|-----|-----|-----|-----|-----|")
    print("|  /  |  A  |  B  |  C  |  D  |  E  |  F  |")
    print("|  1  | *** | *** | *** | *** | *** | *** |")
    print("|  2  | *** | *** | *** | *** | *** | *** |")
    print("|  3  | *** | *** | *** | *** | *** | *** |")
    print("|  4  | *** | *** | *** | *** | *** | *** |")
    print("|-----|-----|-----|-----|-----|-----|-----|")
    column = input("Selection, A - F: ")

    #below loop performs input validation, confirms in put is a, b, c, d, e, f
    #can be either upper or lowercase
    #todo: make it handle string inputs, not just character inputs
    while not(((ord(column) >= 65 and ord(column) <= 70) or (ord(column)>=97 and ord(column)<=102))):
        print("Input rejected, please type a letter A through F\n")
        column = input("Selection, A - F: ")
