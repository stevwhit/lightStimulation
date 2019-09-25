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
GPIO.setmode(GPIO.BCM)
#set all pins to output mode
GPIO.setup(14, GPIO.OUT) #A
GPIO.setup(15, GPIO.OUT) #B
GPIO.setup(18, GPIO.OUT) #C
GPIO.setup(23, GPIO.OUT) #D
GPIO.setup(24, GPIO.OUT) #E
GPIO.setup(25, GPIO.OUT) #F

def columnSet(column, objects, dutyCycles):
    # sets up frequency and duty cycle for that column
    print("You have selected to program Column " + str(column[0]))
    freq = input("Please select the frequency: ")
    dc = input("Please select the duty cycle: ")

    # this is basically a switch case that controls
    # what pin we activate and where the pwm object is stored
    # based on the user-selected column
    if column == "A":
        pin = 14
        offset = 0
    elif column == "B":
        pin = 15
        offset = 1
    elif column == "C":
        pin = 18
        offset = 2
    elif column == "D":
        pin = 23
        offset = 3
    elif column == "E":
        pin = 24
        offset = 4
    elif column == "F":
        pin = 25
        offset = 5

    objects[offset] = GPIO.PWM(pin, freq)
    dutyCycles[offset] = dc

def runPWM(pwmArray):
    # todo: write function that starts PWM for all desired columns
    x = 0 #placeholder code


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
    column = list(input("Selection, A - F: "))

    #below loop performs input validation, confirms in put is a, b, c, d, e, f
    #can be either upper or lowercase
    while not(((ord(column[0]) >= 65 and ord(column[0]) <= 70) or (ord(column[0])>=97 and ord(column[0])<=102))):
        print("Input rejected, please type a letter A through F\n")
        column = input("Selection, A - F: ")

    # these arrays will store current settings in memory
    pwmArray = [0, 0, 0, 0, 0, 0];
    DCArray = [0, 0, 0, 0, 0, 0];
    columnSet(column, pwmArray, DCArray)
    print(DCArray)
