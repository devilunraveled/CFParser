import sys
sys.path.insert( 0, '../parser/')

import os
import siteparser as P
import subprocess
from datetime import date

skeleton = ""

def resetSkeleton( heading ):
    global skeleton

    skeleton = ""

    if heading == '' :
        heading = "CodeForces Problem"

    packages = ["inputenc", "xcolor", "amsmath"]
    # Adding the necessary packages.
    skeleton = "\documentclass{article}"
    for i in packages :
        skeleton += "\n\\usepackage{%s}" % (i)
    #Title, Date
    skeleton += "\n\\title{%s}" % ( heading )
    skeleton += "\n\\date{%s}" % ( date.today().strftime("%B %d, %Y") )
    skeleton += "\n\\author{}"
    
    #Constraints, title etc.
    skeleton += "\n\\begin{document}"
    skeleton += "\n\\maketitle"

def purifySyntax( string ):
    htmlSyntax = ["$$$", "&lt", "&gt", "&amp", "&quot", "&apos", "&cent", "&pound", "&yen", "&euro", "&copy", "&reg", "\n", " ", "\\xrightarrow", "\\xleftarrow" ]
    change = ["$", "<", ">", "&", ' " ', " ' ", "¢", "£", "¥", "€", "©", "®", "\\\ ", " ", "\\rightarrow", "\\leftarrow" ]
    
    for i in range ( len(change ) ):
        string = string.replace(htmlSyntax[i], change[i] )

    return string

def createFile( texFile, fileName ):
    try :
        with open( fileName + ".tex", 'w' ) as file :
            file.write( texFile )
        
        command = subprocess.Popen(['pdflatex', fileName + ".tex"])
        command.communicate()
        
        returnCode = command.returncode
        
        if returnCode != 0 :
            os.unlink( fileName + ".pdf")
            raise Exception("Error Creating The PDF File")

        unwanted = [".tex", ".log", ".aux"]
        for extension in unwanted :
            os.unlink( fileName + extension )
        
        return 0
    except :
        return 1

def createTex( problem, heading ) :
    global skeleton
    
    resetSkeleton( heading )

    skeleton += "\n\\section*{%s}" % ( problem.problemName )
    skeleton += "\n\\subsection*{Constriants}"
    skeleton += "\n\\textbf{Time Limit}"
    skeleton += "\n%d seconds" % ( problem.timeLimit )
    skeleton += "\n\\hfill"
    skeleton += "\n\\textbf{Memory Limit}"
    skeleton += "\n%d MB" % ( problem.memoryLimit )
    #Constraints and Headers are done uptil now.

    #Adding the problem statement
    skeleton += "\n\\subsubsection*{Problem Statement}"
    skeleton += "\n\\paragraph{}"
    skeleton += purifySyntax(problem.problemStatement).replace("\\\ ","\n\n").strip()
    
    #Adding the I/O Descriptions if they exist
    if problem.inputDescription != "" :
        skeleton += "\n\\paragraph{}"
        skeleton += "\n\\subsubsection*{Input Description}"
        skeleton += purifySyntax( problem.inputDescription ).replace("\\\ ","\n\n").strip()
    if problem.outputDescription != "" :
        skeleton += "\n\\paragraph{}"
        skeleton += "\n\\subsubsection*{Output Description : }"
        skeleton += purifySyntax( problem.outputDescription ).replace("\\\ ","\n\n").strip()
    
    #Adding Example Inputs/Outputs
    skeleton += "\n\\subsection*{Examples}"
    for i in range ( len( problem.inputData ) ) :
        skeleton += "\\fbox{\\parbox{\\textwidth}{%"
        skeleton += "\n\\subsubsection*{Input}"
        skeleton += purifySyntax( problem.inputData[i] )
        skeleton += "\n\\subsubsection*{Output}"
        skeleton += purifySyntax( problem.outputData[i] )
        skeleton += "\n}}"
    #Adding a note if it exists
    if problem.note != "" :
        skeleton += "\subsubsection*{Note}"
        skeleton += purifySyntax( problem.note )

    skeleton += "\n\\end{document}"
    
    # print(skeleton)
    return skeleton

def makePDF( problemLink, fileName, contest = 0 ):
    problem = P.Problem()
    problem = P.parser( problemLink ) #The Problem object is stored in the variable problem.
    #Creating the data that is to be written in the .tex file.
    # print( problem )
    texFile = createTex( problem, "" )
    
    # print( problem )
    if contest :
        return skeleton
    else :
        createFile( texFile, fileName )
    

def createContestPDF( problemlinks, contestName ):
    global skeleton

    for link in problemlinks :
        makePDF( link, contestName, 1 )
    
    return createFile( skeleton )
    
# problemLink = "https://codeforces.com/problemset/problem/1703/C"

# print( problem )
# makePDF( problemLink, "Sample" )
