# The following piece of code is used to get all the different types of user data possible
# Currently Includes : 
# ->Get Current Rating Of a User

import requests as R
# Since we are using CodeForces API for this, we are going to send requests.


class Colors : 
    Base = "\033[1;"
    RESET = "\033[39m"
    GREY = Base + "30"
    GREEN = Base + "32m"
    CYAN = Base + "36m"
    BLUE = "\033[38;5;26m"
    VIOLET = "\033[38;5;206m"
    ORANGE = "\033[38;5;214m"
    RED = Base + "31m"
    BLACK = Base + "30m"

username = input("Enter The Username : ")

def getRatingFromText( contestHistory ):
    rating = ""
    for i in range (-4,-8,-1):
        if contestHistory[i] == ':':
            break
        else :
            rating = contestHistory[i] + rating
    return rating
    

def createRank( rating, handle ):
    RESET = Colors.RESET

    if rating < 1200 :
        handle = Colors.GREY + handle + RESET
    elif rating < 1400 :
        handle = Colors.GREEN + handle + RESET
    elif rating < 1600 :
        handle = Colors.CYAN + handle + RESET
    elif rating < 1900 :
        handle = Colors.BLUE + handle + RESET
    elif rating < 2200 : 
        handle = Colors.VIOLET + handle + RESET
    elif rating < 2400 :
        handle = Colors.ORANGE + handle + RESET
    elif rating < 3000 :
        handle = Colors.RED + handle + RESET
    else :
        handle = Colors.BLACK + handle[0] + Colors.RED + handle[1:] + RESET

    return handle

def getRating( UserName ):
    BaseURL = "https://codeforces.com/api/"
    MethodName = "user.rating"
    data = R.get( BaseURL + MethodName + "?handle=" + UserName )
    # Constructing Codeforces Request, as described in the API.
    userRating = getRatingFromText( data.text )

    rating = int(userRating)
    
    UserName =  createRank( rating, UserName )

    # print( "Current Rating of " + UserName + " : " + userRating )
    
    return userRating
