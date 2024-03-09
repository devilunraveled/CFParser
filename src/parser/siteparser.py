#Given a link to a problem, that will lead to it's page in 
#the codeforces website, parse the problem into a Problem Object.
from urllib.request import Request, urlopen
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
    inputData = []
    outputData = []
    note = ''

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
        for i in range ( len(self.inputData) ) :
            string += "Input : \n" + self.inputData[i]
            string += '\n'
            string += "Output : \n" + self.outputData[i]
            string += '\n'
        if self.note :
            string += "Note : \n" + self.note
        return string
    def __init__(self):
        self.problemName = ""
        self.problemStatement = ""
        self.memoryDesc = ""
        self.memoryLimit = 0
        self.timeDesc = ""
        self.timeLimit = 0
        self.inputDescription = ""
        self.outputDescription = ""
        self.inputData = []
        self.outputData = []
        self.note = ''

def extractProblemTitle( problemHTML, problem, inputTitleTag, outputTitleTag ):
    # print(problemHTML)
    found = 0
    for child in problemHTML.descendants :
        try :
            if "class" in child.attrs.keys() and "title" in child["class"] :
                if found == 0 :
                    problem.problemName = child.text
                    found += 1
                elif 'input' in child.parent["class"]:
                        inputTitleTag.append(child)
                        found += 1
                else :
                    if 'output' in child.parent["class"]:
                        outputTitleTag.append(child)
        except :
            continue
    
    # print(inputTitleTag)
    # print(outputTitleTag)
    return problem

def extractProblemConstraints( problemHTML, problem ):
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
    # print(problem.timeLimit)
    # print(problem.memoryLimit)

    return problem

def extractProblemStatement( problemHTML, problem ):
    # print(problemHTML)
    while True :
        try :
            if ( "class" in problemHTML.attrs.keys() and "header" in problemHTML["class"] ) :
                # problemHTML = problemHTML.next_element
                break
            problemHTML = problemHTML.next_element
        except :
            problemHTML = problemHTML.next_element
    
    ufProblem = str( problemHTML.next_sibling )
    
    ufProblem = aLilBetter( ufProblem )
    
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
    
    return problem


def aLilBetter( s ) :
    horribleProgrammingPractice = ['<span class="mn" id="MathJax-Span-97" style="font-size: 70.7%; font-family: MathJax_Main;">4</span>', 
                                   '<span class="mi" id="MathJax-Span-142" style="font-size: 70.7%; font-family: MathJax_Math; font-style: italic;">']
    somewhatTolerablePractice = ['<span class="mn" id="MathJax-Span-97" style="font-size: 70.7%; font-family: MathJax_Main;">^',
                                 '<span class="mi" id="MathJax-Span-142" style="font-size: 70.7%; font-family: MathJax_Math; font-style: italic;">_']
    for i in range ( 0, len(horribleProgrammingPractice) ) :
        crap = horribleProgrammingPractice[i]
        kindaCrap = somewhatTolerablePractice[i]
        s.replace(crap,kindaCrap)
    return s;

def extractIODescription( problemHTML, problem ):
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
   
    inputDesc = aLilBetter( inputDesc )

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

    outputDesc = aLilBetter( outputDesc )
    
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

    try :
        noteInfo = ""
        noteDesc = str( noteTag.parent )

        noteDesc = aLilBetter( noteDesc )
        
        insideTag = False
        started = False

        for i in range ( len( noteDesc ) ) :
            character = noteDesc[i]
            if character == '<' :
                insideTag = True
                if i < len( noteDesc ) - 1 and noteDesc[i + 1] == 'p' :
                    noteInfo += '\n'
                    i += 1
                    started = True
            elif character == '>' :
                insideTag = False
            elif not(insideTag) and started:
                noteInfo += character
    except :
        noteInfo = ""

    problem.outputDescription = outputInfo.strip()
    problem.inputDescription = inputInfo.strip()
    problem.note = noteInfo.strip()

    return problem
    
def extractProblemInput( inputTitleTag, problem ) :

    for i in range ( len(inputTitleTag) ):
        inputData = str( inputTitleTag[i].next_sibling )
        
        counter = 1
        insideTag = False
        inpData = ""

        for i in range ( len(inputData) ):
            character = inputData[i]

            if character == '<':
                insideTag = True
                counter = 1 - counter
                if ( counter == 0 ) :
                    inpData += '\n'
            elif character == '>':
                insideTag = False
            elif not(insideTag):
                inpData += character
          
        problem.inputData.append( inpData.strip() )
    return problem

def extractProblemOutput( outputTitleTag, problem ):

    for i in range ( len( outputTitleTag ) ):
        outputData = str( outputTitleTag[i].next_sibling.text )
        problem.outputData.append(outputData.strip())
    
    return problem

def extractProblemInfo( problemHTML, problem, inputTitleTag, outputTitleTag ):
    problem = extractProblemTitle( problemHTML, problem, inputTitleTag, outputTitleTag )
    problem = extractProblemConstraints( problemHTML, problem )
    problem = extractProblemStatement( problemHTML, problem )
    problem = extractIODescription( problemHTML, problem )
    problem = extractProblemInput( inputTitleTag, problem )
    problem = extractProblemOutput( outputTitleTag, problem )
    print("Problem : ") 
    print(problem)

    return problem

def parser( link ):

    print(f"Processing : {link}")
    print("What")
    hdr = {
        'User-Agent': 'Chrome/58.0.3029.110',
        'Referer': link
    }
    print("The")

    try:
        req = Request(link, headers=hdr)
        fp = urlopen(req)
        html = fp.read().decode('utf-8')
        fp.close()
        problem = Problem()
        inputTitleTag = []
        outputTitleTag = []
        htmlObject = BeautifulSoup(html, 'html.parser')

        problemTag = ""

        for child in htmlObject.find_all('div'):
            if "class" in child.attrs.keys() and "problem-statement" in child["class"]:
                problemTag = child
        #Now, we have found at what point, the search should begin for the problem statement.

        return extractProblemInfo( problemTag, problem, inputTitleTag, outputTitleTag )
    except HTTPError as e:
        print("HTTP Error:", e.code, e.reason)
    except URLError as e:
        print("URL Error:", e.reason)
    except Exception as e:
        print("An error occurred:", str(e))
    

inputTitleTag = []
outputTitleTag = []

# print( problem )
