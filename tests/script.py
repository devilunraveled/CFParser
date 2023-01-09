with open( 'problems', 'w') as file:
    for i in range (1700,1750):
        for j in "ABCD":
            file.write(str(i) + " " + j + "\n" )

