import hashlib, uuid, requests, json

def createHash ( password, username ):
  # First, we create a randomly generated salt to be used in the hashing process
  salt = uuid.uuid4().hex
  # Next, we encode both the password and the salt as utf-8 before we combine them together and create their hash
  hashed_pass = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
  # We set the URL for our API here
  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/"
  # Here we create the request body that we will send to the API
  params = {"username": username, "hash": hashed_pass, "salt": salt}
  # Next, we send the request to the API and put the response information into the variable 'r'
  r = requests.post(API, json.dumps(params))
  # Finally, the status code is returned by the function
  return {r.status_code}

def verifyUser ( password, username ):
  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/salt"
  params = {"username": username}
  r = requests.post(API, json.dumps(params))

  hashed_pass = hashlib.sha512(password.encode('utf-8') + r.json()['body'].replace('"', '').encode('utf-8')).hexdigest()

  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/verifyuser"
  params = {"username": username, "password": hashed_pass}
  r = requests.post(API, json.dumps(params))
  
  return r.json()['body']

print(createHash("France", "AliC"))
print(verifyUser("France", "AliC"))
