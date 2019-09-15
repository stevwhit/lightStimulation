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
