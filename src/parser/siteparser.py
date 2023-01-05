#Given a link to a problem, that will lead to it's page in 
#the codeforces website, parse the problem into a Problem Object.
import urllib.request as urlreq
from bs4 import BeautifulSoup

class Problem :
    problemName = ''
    problemStatement = ''
    memoryLimit = 0
    timeLimit = 0
    inputDescription = ''
    outputDescription = ''
    inputData = ''
    outputData = ''

link = "https://codeforces.com/problemset/problem/1779/D"

problem = Problem()


def extractProblemTitle( problemHTML ):
    global problem
    global inputTitleTag
    global outputTitleTag

    found = 0
    for child in problemHTML.descendants :
        try :
            if "class" in child.attrs.keys() and "title" in child["class"] :
                if found == 0 :
                    problem.problemName = child.text
                    found += 1
                elif found == 1 :
                    inputTitleTag = child
                    found += 1
                elif found == 2 :
                    outputTitleTag = child
        except :
            continue
    
    return problem.problemName

def extractProblemInput( inputTitleTag ) :
    inputData = str( inputTitleTag.next_sibling )
    global problem
    
    # print(inputData)

    counter = 1
    insideTag = False
    
    for i in range ( len(inputData) ):
        character = inputData[i]

        if character == '<':
            insideTag = True
            counter = 1 - counter
            if ( counter == 0 ) :
                problem.inputData += '\n'
        elif character == '>':
            insideTag = False
        elif not(insideTag):
            problem.inputData += character
      
    problem.inputData = problem.inputData.strip()
    return problem.inputData

def extractProblemOutput( outputTitleTag ):
    global problem
    outputData = str( outputTitleTag.next_sibling.text )
    problem.outputData = outputData.strip()

    return problem.outputData

def extractProblemInfo( problemHTML ):
    
    problemTitle = extractProblemTitle( problemHTML )
    print( "Title : ", problemTitle )
    #problemConstraints = extractProblemConstraints( problemHTML )
    #problemStatement = extractProblemStatement( problemHTML )
    problemInput = extractProblemInput( inputTitleTag )
    problemOutput = extractProblemOutput( outputTitleTag )

    datastring = str( problemHTML )

    # datastring = str( problemHTML )
    problemStatement = "" 
    insideTag = False
    
    # print( problemHTML )

    for i in range ( len(datastring) ) :
        character = datastring[i]

        if character == '<' :
            insideTag = True
            if i < len(datastring) - 1 and datastring[i+1] == 'p':
                i += 1
                problemStatement += '\n'
        elif character == '>' :
            insideTag = False
        elif not(insideTag) :
            problemStatement += character
        
    return problemStatement

def parser( link ): 

    fp = urlreq.urlopen(link)
    html = fp.read().decode('utf-8')
    fp.close()
    # print(html)

    htmlObject = BeautifulSoup(html, 'html.parser')

    problemTag = ""

    for child in htmlObject.find_all('div'):
        if "class" in child.attrs.keys() and "problem-statement" in child["class"]:
            problemTag = child
#Now, we have found at what point, the search should begin for the problem statement.

    return problemTag

problemHTML = parser( link )

inputTitleTag = problemHTML
outputTitleTag = problemHTML

extractProblemInfo( problemHTML ) 
