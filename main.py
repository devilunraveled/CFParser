import sys 
sys.path.insert(0, './src/errors/')
sys.path.insert(0, './src/output/')
sys.path.insert(0, './src/parser/')

import pdfMaker as Pm
import contestParser as Cp

welcomeMessage = "Hello, thanks for using CFParser"

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

            for code in problemCodes :
                problemLinks.append(CodeForces + Contest + Problem + code)
                # print(problemLinks[-1])
            # contestName = "Contest " + str(contestCode)
            # Pm.createContestPDF( problemLinks, contestName)
        except Exception as e:
            print(e)

            
def oldContestProblemsPDF() :
    contestCode = int(input("Enter The Contest Number ( e.g. 178, 1695)" ))
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
            print(e)


def options():
    print("Enter 1 to Solve A problem of your choice")
    print("Enter 2 to Get A Running Contests' Problems")
    print("Enter 3 to Get an old Contests' Problems")
    print("Enter 0 to exit")


def displayClosingMessage() :
    return 

def displayRandomMessage() :
    return

def CFParser() :
    print( welcomeMessage )
    functionList = [ singleProblemPDF, liveContestProblemsPDF, oldContestProblemsPDF ]
    while True :
        options() #Give the available functions to the user.
        
        choice = int( input ("Enter Your Choice : ") )
        
        if choice == 0 :
            displayClosingMessage()
            break
        
        if choice < 0 :
            displayRandomMessage()
            break

        if choice <= len( functionList ) :
            functionList[ choice - 1 ]()
        
if __name__ == '__main__' :
    CFParser()
