import sys # For accessing the system information, taking argument from command line args.
from siteparser import parseURL

mainUrl = "https://codeforces.com/"
contest = "contest/"
problem = "problem/"
problemset = "problemset/"
URL = "";

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
                URL = mainUrl + contest + str(contestNum) + "/" + problem + problemCode
                print("URL : ", URL)
                parseURL(URL)
            else:
                print(command)
                printError()
        else:
            printError()
    elif lengthOfCommand == 3 and command[1].lower() == 'p' :
        if command[2].isalnum():
            j = 0
            for i in command[2]:
                if not i.isnumeric():
                    break
                else:
                    j+=1
            problemCode = command[2][j:]
            problemNum = command[2][:j]
            URL = mainUrl + problemset + problem + problemNum + "/" + problemCode 
            print("URL : " + URL)
            parseURL(URL)
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
