# main code for light stimulatio project
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
