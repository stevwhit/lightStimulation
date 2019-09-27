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
#change

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
GPIO.setwarnings(False)

def pinAndOffset(col):
    # function to get pin and offset from column value
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

    return [pin, offset]

def pinFromOffset(offset):
    if offset == 0:
        pin = 14
    elif offset == 1:
        pin = 15
    elif offset == 2:
        pin = 18
    elif offset == 3:
        pin = 23
    elif offset == 4:
        pin = 24
    elif offset == 5:
        pin = 25

    return pin

def columnSet(column, objects, dutyCycles):
    # sets up frequency and duty cycle for that column
    print("You have selected to program Column " + column)
    freq = float(input("Please select the frequency: "))
    dc = float(input("Please select the duty cycle: "))

    [pin, offset] = pinAndOffset(column)
    objects[offset] = GPIO.PWM(pin, freq)
    dutyCycles[offset] = dc

def runPWM(pwmArray, DCArray):
    x = input("Press enter to begin the PWM on all programmed channels: ")
    # this for loop will start all PWM objects with a duty cycle
    # that is not negative (i.e. the initial value)
    for ii, each in enumerate(DCArray):
        if each >= 0:
            pwmArray[ii].start(each)

    x = input("Press enter to stop PWM on all programmed channels: ")



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

    #column value MUST be converted to a string
    column = str(column[0])
    # these arrays will store current settings in memory
    pwmArray = [-1, -1, -1, -1, -1, -1];
    DCArray = [-1, -1, -1, -1, -1, -1];
    columnSet(column, pwmArray, DCArray)

    #todo: add input validation here for yes or no
    print("Would you like to set another column?")
    response = input("Type Yes or No: ")
    if response == "Yes":
        setting = True
    else:
        setting = False

    while(setting):
        column = list(input("Selection, A - F: "))
        while not(((ord(column[0]) >= 65 and ord(column[0]) <= 70) or (ord(column[0])>=97 and ord(column[0])<=102))):
            print("Input rejected, please type a letter A through F\n")
            column = input("Selection, A - F: ")
        column = str(column[0])
        columnSet(column, pwmArray, DCArray)
        print("Would you like to set another column?")
        response = input("Type Yes or No: ")
        if response == "Yes":
            setting = True
        else:
            setting = False

    runPWM(pwmArray, DCArray)
