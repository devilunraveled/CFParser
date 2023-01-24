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
    #\usepackage[a4paper, total={6in, 8in}]{geometry}
    packages = ["inputenc", "fontenc", "xcolor", "amsmath", "geometry"]
    encoding = [ "", "T1", "", "", "a4paper, total={6in, 10in}"]
    # Adding the necessary packages.
    skeleton += "\documentclass{article}"
    for i in range (0,len(packages)) :
        pack = packages[i] 
        if encoding[i] == "" :
            skeleton += "\n\\usepackage{%s}" % (pack)
        else :
            skeleton += "\n\\usepackage[%s]{%s}" % (encoding[i], pack)
    #Title, Date
    skeleton += "\n\\title{%s}" % ( heading )
    skeleton += "\n\\date{%s}" % ( date.today().strftime("%B %d, %Y") )
    skeleton += "\n\\author{}"
    
    #Constraints, title etc.
    skeleton += "\n\\begin{document}"
    skeleton += "\n\\maketitle"
    
    #Custom Commands
    newCommands = ["\\lt", "\\gt" ]
    actualCommands = ["\\ensuremath <", "\\ensuremath >"]
    for i in range (0,len(newCommands)):
        skeleton += "\n\\newcommand{%s}{%s}" % ( newCommands[i], actualCommands[i] )
   
    return

def purifySyntax( string ):
    htmlSyntax = ["$$$", "&lt", "&gt", "&amp", "&quot", "&apos", "&cent", "&pound", "&yen", "&euro", "&copy", "&reg", "\n", " ", "\\xrightarrow", "\\xleftarrow", "≤", "≥" ]
    change = ["$", "<", ">", "&", ' " ', " ' ", "¢", "£", "¥", "€", "©", "®", "\\\ ", " ", "\\rightarrow", "\\leftarrow", "$\\leq$", "$\\geq$"]
    
    for i in range ( len(change ) ):
        string = string.replace(htmlSyntax[i], change[i] )

    return string

def createFile( texFile, fileName ):
    try :
        with open( fileName + ".tex", 'w' ) as file :
            file.write( texFile )
        
        command = subprocess.Popen(['pdflatex', '-quit', fileName + ".tex"], stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        command.communicate()
        
        returnCode = command.returncode
        print("Return Code : ", returnCode)
        
        if returnCode != 0 :
            os.unlink( fileName + ".pdf")
            raise Exception("Error Creating The PDF File")

        unwanted = [".tex", ".log", ".aux"]
        for extension in unwanted :
            os.unlink( fileName + extension )
        
        return 0
    except :
        return 1

def createTex( problem, heading, mode = 1 ) :
    global skeleton
    
    if mode == 0 :
        print("????")
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
        skeleton += "\n"
        skeleton += "\\fbox{\\parbox{\\dimexpr\\linewidth-2\\fboxsep-2\\fboxrule}{%"
        skeleton += "\n\\textbf{Input}\n\n"
        skeleton += purifySyntax( problem.inputData[i] )
        skeleton += "\n\n\\textbf{Output}\n\n"
        skeleton += purifySyntax( problem.outputData[i] )
        skeleton += "}}"
    #Adding a note if it exists
    if problem.note != "" :
        skeleton += "\subsubsection*{Note}"
        skeleton += purifySyntax( problem.note )
    
    if mode == 0 :
        skeleton += "\n\\end{document}"
    
    # print(skeleton)
    return skeleton

def makePDF( problemLink, fileName, contest = 0):
    problem = P.Problem()
    problem = P.parser( problemLink ) #The Problem object is stored in the variable problem.
    #Creating the data that is to be written in the .tex file.
    # print( problem )
    texFile = createTex( problem, "", contest )
    
    if contest == 1 :
        return 
    else :
        createFile( texFile, fileName )
    

def createContestPDF( problemlinks, contestName ):
    global skeleton
    resetSkeleton( '' )
    #In this case, skeleton needs to be reset only once globally.
    try :
        for link in problemlinks :
            makePDF( link, contestName, 1 )
            skeleton += "\n\\newpage" 
        skeleton += "\n\\end{document}"
        return createFile( skeleton, contestName )
    except Exception as e:
        print(e)
# problemLink = "https://codeforces.com/problemset/problem/1703/C"

# print( problem )
# makePDF( problemLink, "Sample" )
