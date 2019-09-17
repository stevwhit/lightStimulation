# main code for light stimulatio project

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

#import RPi.GPIO as GPIO

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
