import sys # For accessiing the system information, taking argument from command line args.
from urllib.request import Request, urlopen # For parsing and downloading the html from a site.

mainUrl = "https://codeforces.com/"
contest = "contest/"
problem = "problem/"

def printError( ):
    print("Errenous Command")

def notValid( command ):
    if len(command) == 1 :
        return 1
    else :
        return 0
# Minimum number of args is 1.

def inputHandler():
    command = sys.argv
    lengthOfCommand = len( command )

    if notValid( command ):
        printError() #-> A separate function to print out errors.
    # Otherwise.
    if lengthOfCommand == 4 and command[1].lower() == 'c':   #For contest.
        if command[2].isnumeric():
            contestNum = int(command[2])
            if command[3] == '-all':
                print("Do recursively for all problems.")
            elif command[3].isalpha() :
                problemCode = command[3]
                print("Contest num : ", contestNum, "Problem : ", problemCode)
            else:
                print(command)
                printError()
        else:
            printError()
    elif lengthOfCommand == 3 and command[1].lower() == 'p' :
        if command[2].isalnum():
            problemCode = command[2][-1]
            problemNum = command[2][:-1]
            print("Problem Number : ",problemNum," Code : ",problemCode)
        else:
            printError()
    else:
        printError()

# The program is not as an subroutine from another file but from the command line itself.

def main():
    inputHandler()
    #Handle the input and error checking in the input.
    

if __name__ == '__main__': 
    main()
