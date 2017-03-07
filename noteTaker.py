#!/usr/bin/python
__author__ = "Henry Blackie"
__copyright__ = "Copyright (C) 2017 Henry Blackie"
__license__ = "MIT Licence"
__version__ = "0.1"

def mainMenu(menuSelection):
    menu = {}
    menu['1'] = "New Case Notes"
    menu['2'] = "Add To Existing Case Notes"
    menu['3'] = "Read Case Note"
    menu['99'] = "Exit"

    options = menu.keys()
    options.sort()
    
    while True:
        for entry in options:
            print entry + '\t' + menu[entry]

        menuSelection = raw_input(">> ")
        if menuSelection in menu:
            return menuSelection
        else:
            print "Invalid input"

def newNote():
    # ask user for case name
    caseName = raw_input("Case Name >> ")

    noteTaking(caseName)

def openNote():
    # ask user for case name
    caseName = raw_input("Case Name >> ")

    # open file with case name
    textFile = open(caseName, 'r')

    # print contents of text file
    for line in textFile:
        print line

    textFile.close()

    noteTaking(caseName)

def readNote():
    # ask user for case name
    caseName = raw_input("Case name >> ")

    # open file with case name
    textFile = open(caseName, 'r')

    # print contents of text file
    for line in textFile:
        print line

    textFile.close()

    print("\n*** END OF CASE NOTE ***\n")

def noteTaking(caseName):
    import time # used for getting date/time
    entry = ""

    textFile = open(caseName, 'a')

    print("Enter 'EXIT' to stop")
    
    while entry != "EXIT":
        entry = raw_input(">> ")

        if entry != "EXIT":
            textFile.write(time.strftime("%Y/%m/%d %H:%M:%S\t" + entry + '\n'))
            
    textFile.close()
    
def main():

    menuSelection = 0

    while int(menuSelection) != 99:
        # ask user what they want to do
        menuSelection = mainMenu(menuSelection)

        # perform action based on selection
        if int(menuSelection) == 1:
            newNote()
        elif int(menuSelection) == 2:
            openNote()
        elif int(menuSelection) == 3:
            readNote()
        elif int(menuSelection) == 99:
            print("Exiting note taker...")

if __name__ == '__main__':
    main()
