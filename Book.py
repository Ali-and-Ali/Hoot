import requests, json
API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/book"

def addBook( title, author, genre, ISBN, quantity ):
    params = {"title": title, "author": author, "genre": genre, "ISBN": ISBN, "quantity": quantity, "action": "addBooks"}
    r = requests.post(API, json.dumps(params))
    return r.json()['bookID']

def deleteBook( title, author ):
    params = {"title": title, "author": author, "action": "deleteBooks"}
    r = requests.post(API, json.dumps(params))
    return r.status_code

def updateBook( title, author, field ):
    params = {"title": title, "author": author, "field": field, "action": "updateBooks"}
    r = requests.post(API, json.dumps(params))
    return r.status_code

def getBookTable():
    params = {"action": "getBookTable"}
    r = requests.get(API, params)
    return r.json()