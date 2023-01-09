import sys
sys.path.insert(0,'../src/output')
sys.path.insert(0,'../src/parser')

import pdfMaker as P

link = "https://codeforces.com/problemset/problem/%s/%s"

def normalTest():
    with open('problems', 'r' ) as f :
        try :
            while True :
                problemLink = link
                line = f.readline()
                
                if not line :
                    break
                
                args = line.strip().split(' ')
                problemLink = problemLink % ( args[0], args[1] )
                P.makePDF( problemLink, "Problem%s-%s" % ( args[0], args[1] ) )
        except Exception as e :
            print(e)
            print( f.readline() )

normalTest()
