# DISPLAYINFO :
# Name : First and Last Name
# Location : City, Country 
# Rating : current rating (max rating)
# Rank : current rank (max rank)
# Last Online : Time and Date
# Registered  : Time and Date
# Contribution : con.

from requesthandler import *
from output import colors 
from errors import requestErrors as E
import sys
from datetime import datetime

# Whatever data is requested, this function can be called to retrieve the entire 
# userdata made available by the CodeForces API.

if not(__debug__) :
    sys.tracebacklimit = 0
# Unless debugging, custom exceptions won't have tracebacks. 

def getAllData( username ):
    requestName = createRequest( "user.info" ,  username )
    if E.Errenous( requestName ) :
        raise Exception('The username : %s is not valid', username )

    data = processRequest( requestName )
    if data.status_code != 200 :
        raise Exception( 'Could Not Retrive Data for the given user' )
    
    return data.json()["result"][0] 


# The function returns a dictionary of the various properties of the json 
# object used by codeforces. 


#A dictionary of properties and its values is given to the function. 
def displayUserData( data ):
    try : 
        name = ""
        location = ""
        if "firstName" in data.keys() and data["firstName"].isalpha() :
            name = data["firstName"]
        if "lastName" in data.keys() and data["lastName"].isalpha() :
            name = name + " " + data["lastName"]
        if "city" in data.keys() :
            location = data["city"]
        if "country" in data.keys() :
            location = location + ", " + data["country"]
        if "rating" not in data.keys() :                            #For unrated users, the rating field is not created.
            data["rating"] = data["maxRating"] = 0
            data["rank"] = data["maxRank"] = 'Unranked'

        if name != "" :
            print("Name : " + name )
        if location != "" :
            print("Location : " + location )
        print( 'Rating : %d ( %d ) ' % ( data["rating"], data["maxRating"] ) )
        print( 'Rank : %s ( %s )' % ( data["rank"], data["maxRank"] ) )
        print( "Last Online : " , datetime.fromtimestamp(data["lastOnlineTimeSeconds"]).strftime("%A, %B %d, %Y %I:%M:%S") )
        print( "Registered : " , datetime.fromtimestamp(data["registrationTimeSeconds"]).strftime("%A, %B %d, %Y %I:%M:%S") )
        print( 'Contribution : %d' % ( data["contribution"] ) )
    except Exception as e :
        print("Data Could Not Be Succesfully retrieved for the given user.")

while( True ):
    username = input("Enter The username : ")
    displayUserData( getAllData( username ) )
