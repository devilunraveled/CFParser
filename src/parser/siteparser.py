#Given a link to a problem, that will lead to it's page in 
#the codeforces website, parse the problem into a Problem Object.
import urllib.request as urlreq
from bs4 import BeautifulSoup

class Problem :
    problemName = ''
    problemStatement = ''
    memoryDesc = ''
    memoryLimit = 0
    timeDesc = ''
    timeLimit = 0
    inputDescription = ''
    outputDescription = ''
    inputData = ''
    outputData = ''

    def __str__(self):
        string = "Title : " + self.problemName
        string += '\n'
        string += "Memory Limit : " + str( self.memoryDesc )
        string += '\n'
        string += "Time Limit : " + str( self.timeDesc )
        string += '\n'
        string += "Problem Statement : \n" + self.problemStatement
        string += '\n'
        string += "Input Description : \n" + self.inputDescription
        string += '\n'
        string += "Output Description : \n" + self.outputDescription
        string += '\n'
        string += "Input : \n" + self.inputData
        string += '\n'
        string += "Output : \n" + self.outputData
        return string

link = "https://codeforces.com/problemset/problem/1768/B"

problem = Problem()

def purifySyntax( string ):
    htmlSyntax = ["$$$", "&lt", "&gt", "&amp", "&quot", "&apos", "&cent", "&pound", "&yen", "&euro", "&copy", "&reg"]
    change = ["$", "<", ">", "&", ' " ', " ' ", "¢", "£", "¥", "€", "©", "®"]
    
    for i in range ( len(change ) ):
        string = string.replace(htmlSyntax[i], change[i] )

    return string


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

def extractProblemConstraints( problemHTML ):
    global problem
    
    for child in problemHTML.descendants :
        try :
            if "class" in child.attrs.keys() and "time-limit" in child["class"] :
                timeString = str( child.next_element.next_element.next_element ).split(" ")
                problem.timeDesc = " ".join(timeString)
                problem.timeLimit = int( timeString[0] )
        except :
            continue

    for child in problemHTML.descendants :
        try :
            if "class" in child.attrs.keys() and "memory-limit" in child["class"] :
                memoryString = str( child.next_element.next_element.next_element ).split(" ")
                problem.memoryDesc = " ".join(memoryString)
                problem.memoryLimit = int( memoryString[0] )
        except :
            continue

    return [problem.timeLimit, problem.memoryLimit]

def extractProblemStatement( problemHTML ):
    global problem

    while ( True ) :
        # print( problemHTML )
        try :
            if ( "class" in problemHTML.attrs.keys() and "output-file" in problemHTML["class"] ) :
                problemHTML = problemHTML.next_element
                break
            else :
                problemHTML = problemHTML.next_element
        except :
            problemHTML = problemHTML.next_element
        
    ufProblem = str( problemHTML.next_sibling.next_element )
    insideTag = False
    string = ""

    for i in range ( len(ufProblem) ) :
        character = ufProblem[i]
        if character == '<' :
            insideTag = True
            if i < len( ufProblem ) - 1 and ufProblem[i + 1] == 'p' :
                string += '\n'
                i += 1
        elif character == '>' :
            insideTag = False
        elif not(insideTag):
            string += character
    
    problem.problemStatement = string.strip()

def extractIODescription( problemHTML ):
    global problem

    counter = 0

    for child in problemHTML.descendants :
        try :
            if "class" in child.attrs.keys() and "section-title" in child["class"] :
                if counter == 0 :
                    counter += 1
                    inputDescTag = child
                elif counter == 1 :
                    counter += 1
                    outputDescTag = child
                elif counter == 2:
                    counter += 1
                else :
                    noteTag = child
        except :
            continue

    inputInfo = ""
    inputDesc = str(inputDescTag.parent)

    insideTag = False
    started = False

    for i in range ( len( inputDesc ) ) :
        character = inputDesc[i]
        if character == '<' :
            insideTag = True
            if i < len( inputDesc ) - 1 and inputDesc[i + 1] == 'p' :
                inputInfo += '\n'
                i += 1
                started = True
        elif character == '>' :
            insideTag = False
        elif not(insideTag) and started:
            inputInfo += character

    outputInfo = ""
    outputDesc = str( outputDescTag.parent )

    insideTag = False
    started = False

    for i in range ( len( outputDesc ) ) :
        character = outputDesc[i]
        if character == '<' :
            insideTag = True
            if i < len( outputDesc ) - 1 and outputDesc[i + 1] == 'p' :
                outputInfo += '\n'
                i += 1
                started = True
        elif character == '>' :
            insideTag = False
        elif not(insideTag) and started:
            outputInfo += character
     
    problem.outputDescription = outputInfo.strip()
    problem.inputDescription = inputInfo.strip()

def extractProblemInput( inputTitleTag ) :
    inputData = str( inputTitleTag.next_sibling )
    global problem
    
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
    global problem

    problemTitle = extractProblemTitle( problemHTML )
    problemConstraints = extractProblemConstraints( problemHTML )
    problemStatement = extractProblemStatement( problemHTML )
    ioDescription = extractIODescription( problemHTML )
    problemInput = extractProblemInput( inputTitleTag )
    problemOutput = extractProblemOutput( outputTitleTag )
        
    return problem

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

print( problem )
# print( purifySyntax( problem.problemStatement ) )
# print( purifySyntax( problem.inputDescription ) )
# print( purifySyntax( problem.outputDescription ) )
