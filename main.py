import os 
sys.path.insert(0, './src/errors/')
sys.path.insert(0, './src/output/')
sys.path.insert(0, './src/parser/')

import pdfMaker as Pm

welcomeMessage = "Hello, thanks for using CFParser"

CodeForces = "https://codeforces.com/"
ProblemSet = "problemset/problem/"

def makingPDF( ):
    problemCode = input("Enter The Problem Code ( e.g. 1705A, 1696B ) : ") 
    
    problemLink = ""

    if isint(problemCode[-1]) :
        contestCode = problemCode[:-2]
        problemLevel = problemCode[-2:]

    problemLink = CodeForces + ProblemSet + contestCode + '/' + problemLevel

    print( problemLink )

def CFParser() :
    print( welcomeMessage )
    functionList = [ makingPDF ]
    while True :
        print( options )
        choice = int( input ("Enter Your Choice : ") )
        
        if choice <= len( functionList ) :
            functionList[ choice - 1 ]()

if __name__ == '__main__' :
    CFParser()
