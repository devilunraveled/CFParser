import requests as R

BASEURL = "https://codeforces.com/api/"
HANDLE = "?handles="

def createRequest( method, arguments ):
    return BASEURL + method + HANDLE + arguments

def processRequest( requesturl ):
    return R.get( requesturl )
