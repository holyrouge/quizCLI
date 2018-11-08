'''
Program Name: quizCLI
Purpose: Command-line Quizlet

Author: Prangon Ghose
Last Updated: 11/07/2018
'''
import random

#Global Variables
dict = []
userInput = ""

# Class
class entry:
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
    userInput = input("Enter S to begin: ")
    if userInput == "S":
       readInput()
       quiz()
    elif userInput == "0":
        println("You have successfully exited from the program!")
        exit(1)
    elif userInput == "1":
        os.execl(sys.executable, sys.executable, *sys.argv)
    inputFile.close()

def readInput():
    global dict
    inputFile = open('input.txt', 'r+')
    with open('input.txt') as inputFile:
        for line in inputFile:
            myList = line.split(':')
            x = entry(myList[0].strip(), myList[1].strip())
            dict.append(x)

def quiz():
    global userInput
    while userInput != "0" or userInput != "1":
        entryNum = randrange(0, len(dict) - 1)
        println("Definition: " + dict[entryNum].Definition)
        userInput = input("Enter an answer to the definition: ")
        while userInput != dict[entryNum].Answer:
            userInput = input("Please try again or enter R to try another definition: ")
        else:
            if userInput == "R":
                continue
        println("Your correct!")
        continue
    if userInput == "0":
        exit(1)
    elif userInput == "1":
        os.execl(sys.executable, sys.executable, *sys.argv)


# Calling Functions
main()