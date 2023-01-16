import sys 
sys.path.insert(0, './src/errors/')
sys.path.insert(0, './src/output/')
sys.path.insert(0, './src/parser/')

import pdfMaker as Pm

welcomeMessage = "Hello, thanks for using CFParser"

CodeForces = "https://codeforces.com/"
ProblemSet = "problemset/"
Problem = "problem/"
Contest = "contest/"

def makingPDF( ):
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


def options():
    print("Enter 1 to Solve A problem of your choice")
    print("Enter 2 to Get A Contests's Problems")
    print("Enter 0 to exit")


def displayClosingMessage() :
    return 

def displayRandomMessage() :
    return

def CFParser() :
    print( welcomeMessage )
    functionList = [ makingPDF ]
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
