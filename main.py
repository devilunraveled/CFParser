import sys 
sys.path.insert(0, './src/errors/')
sys.path.insert(0, './src/output/')
sys.path.insert(0, './src/parser/')

import pdfMaker as Pm
import contestParser as Cp

welcomeMessage = "Hello, thanks for using CFParser"
line = "\u2500"
side = "\u2502"
topRightCorner = "\u2510"
topLeftCorner = "\u250c"
botRightCorner = "\u2518"
botLeftCorner= "\u2514"
CodeForces = "https://codeforces.com/"
ProblemSet = "problemset/"
Problem = "problem/"
Contest = "contest/"

def singleProblemPDF( ):
    problemCode = input("Enter The Problem Code ( e.g. 1705A, 1696B ) : ") 
    
    problemLink = ""

    if problemCode[-1].isnumeric() :
        contestCode = problemCode[:-2]
        problemLevel = problemCode[-2:]
    else :
        contestCode = problemCode[:-1]
        problemLevel = problemCode[-1]

    problemLink = CodeForces + ProblemSet + Problem + contestCode  + '/' + problemLevel
    # problemLink = CodeForces + Contest + 'problem/' + problemLevel 

    fileName = input("What should be the name of the file? ")

    Pm.makePDF(problemLink, fileName)

def liveContestProblemsPDF() :
    contestCode = int(input("Enter The Contest Number ( e.g. 178, 1695)" ))
    if contestCode < 1 :
        print("Invalid Contest Number")
    else :
        try :
            problemLinks = []
            contestLink = CodeForces + Contest + str(contestCode)
            problemCodes = Cp.contestPageParser( contestLink )
            
            # print(problemCodes)

            for code in problemCodes :
                problemLinks.append(CodeForces + Contest + str(contestCode) + "/" + Problem + code)
                # print(problemLinks[-1])
            contestName = "Contest " + str(contestCode)
            Pm.createContestPDF( problemLinks, contestName)
        except Exception as e:
            print(e)

            
def oldContestProblemsPDF() :
    contestCode = int(input("Enter The Contest Number ( e.g. 178, 1695) : " ))
    if contestCode < 1 :
        print("Invalid Contest Number")
    else :
        try :
            problemLinks = []
            contestLink = CodeForces + Contest + str(contestCode)
            problemCodes = Cp.contestPageParser( contestLink )

            for code in problemCodes :
                problemLinks.append(CodeForces + ProblemSet + Problem + str(contestCode) +  "/" + code)
                print(problemLinks[-1])
            contestName = "Contest " + str(contestCode)
            Pm.createContestPDF( problemLinks, contestName)
        except Exception as e:
            print("Encountered Error : ", e)


def options():
    length = 38
    print(topLeftCorner + line*length + topRightCorner)
    print(f"{side} 1 : Solve a single Problem {' '*9} {side}")
    print(side + line*length + side )
    print(f"{side} 2 : Get A Running Contests' Problems {side}")
    print(side + line*length + side)
    print(f"{side} 3 : Get an old Contests' Problems {' '*2} {side}")
    print(side + line*length + side)
    print(f"{side} 0 : Exit the command line {' '*10} {side}")
    print(botLeftCorner + line*length + botRightCorner)

def displayWelcomeMessage() :
    length = 50
    print(topLeftCorner + line*length + topRightCorner)
    print(f"{side} {' '*7} {welcomeMessage} {' '*7} {side}")
    print(botLeftCorner + line*length + botRightCorner)

def displayClosingMessage() :
    return 

def displayRandomMessage() :
    return

def displayRandomInsult() :
    return

def CFParser() :
    try : 
        displayWelcomeMessage()
        functionList = [ singleProblemPDF, liveContestProblemsPDF, oldContestProblemsPDF ]
        options() #Give the available functions to the user.
        
        choice = int( input ("Enter Your Choice : ") )
        
        if choice == 0 :
            displayClosingMessage()
        elif choice < 0 :
            displayRandomMessage()
        elif choice <= len( functionList ) :
            functionList[ choice - 1 ]()
        else :
            displayRandomMessage()
    except (Exception):
        displayRandomInsult()
if __name__ == '__main__' :
    CFParser()
