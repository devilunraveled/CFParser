import os
import sys
import subprocess

from ..parser import parser
from datetime import date

def purifySyntax( string ):
    htmlSyntax = ["$$$", "&lt", "&gt", "&amp", "&quot", "&apos", "&cent", "&pound", "&yen", "&euro", "&copy", "&reg", "\n" ]
    change = ["$", "<", ">", "&", ' " ', " ' ", "¢", "£", "¥", "€", "©", "®", "\n\n" ]
    
    for i in range ( len(change ) ):
        string = string.replace(htmlSyntax[i], change[i] )

    return string

def createTex( problem, codeAuthor ) :
    packages = ["inputenc", "xcolor"]
    # Adding the necessary packages.
    skeleton = "\documentclass{article}"
    for i in packages :
        skeleton += "\n\\usepackage{%s}" % (i)
    skeleton += "\n\\title{%s}" % ( problem.problemName )
    skeleton += "\n\\author{%s}" % ( codeAuthor )
    skeleton += "\n\\date(%s)" % ( date.today().strftime("%B %d, %Y") )
    skeleton += "\n\\begin{document}"
    skeleton += "\n\\maketitle"
    skeleton += "\n\\section*{Constriants}"
    skeleton += "\n\\subsection*{Time Limit}"
    skeleton += "\n%d seconds" % ( problem.timeLimit )
    skeleton += "\n\\subsection{Memory Limit}"
    skeleton += "\n%d MB" % ( problem.memoryLimit )
    
    print( skeleton )

def makePDF( problemLink ):
    problem = P.parser( problemLink )       #The Problem object is stored in the variable problem.
    createTex( problem )

problemLink = "https://codeforces.com/problemset/problem/1773/A"
