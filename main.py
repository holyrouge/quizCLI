'''
Program Name: quizCLI
Purpose: Command-line Quizlet

Author: Prangon Ghose
'''
import random
from random import randrange
import os
import sys

#Global Variables
dict = []
userInput = ""

# Class Entry
class Entry:
    Answer = ""
    Definition = ""

    def __init(self):
        self.Answer = "Template"
        self.Definition = "Template"

    def __init__(self, ans, definition):
        self.Answer = ans
        self.Definition = definition


# Functions
def main():
    print("""
    Welcome to QuizCLI, the Command Line Quizlet! \n
    Please make sure you have inputted your Answers and Definitions to the input.txt file in the following format: \n
    <Answer>: <Definition> \n
    As a note, you can enter 0 to exit the program or 1 to restart the program.
    After you have completed that, please press enter S to begin. \n
    """)
    userInput = input("Enter S to begin: ").lower()
    if userInput == "s":
       readInput()
       quiz()
    elif userInput == "0":
        print("You have successfully exited from the program!\n")
        exit(0)
    elif userInput == "1":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        print("Invalid Input.\n")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

def readInput():
    global dict
    inputFile = open('input.txt', 'r+')
    with open('input.txt') as inputFile:
        for line in inputFile:
            myList = line.split(':')
            x = Entry(myList[0].strip(), myList[1].strip())
            dict.append(x)
    inputFile.close()

def quiz():
    global userInput
    contFlag = False
    breakFlag = False
    while userInput != "0" or userInput != "1":
        entryNum = randrange(0, len(dict) - 1)
        print("Definition: " + dict[entryNum].Definition + "\n")
        userInput = input("Enter an answer to the definition: ").lower()
        while userInput != dict[entryNum].Answer.lower() or userInput == "r" or userInput == "0" or userInput == "1":
            if userInput == "r":
                contFlag = True
                break
            elif userInput == "0" or userInput == "1":
                breakFlag = True
                break
            else:
                userInput = input("Please try again or enter R to try another definition: ")
                continue
        if contFlag:
            contFlag = False
            continue
        if breakFlag:
            breakFlag = False
            break
        print("Your correct!\n")
    if userInput == "0":
        exit(0)
    elif userInput == "1":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


    # Calling Functions
main()