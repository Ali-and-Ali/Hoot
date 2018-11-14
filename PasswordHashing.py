import hashlib, uuid, requests, json

def createHash ( password, username ):
  # First, we create a randomly generated salt to be used in the hashing process
  salt = uuid.uuid4().hex
  # Next, we encode both the password and the salt as utf-8 before we combine them together and create their hash
  hashed_pass = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
  # We set the URL for our API here
  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/"
  # Here we create the request body that we will send to the API, it contains the username, hashed password, and salt
  params = {"username": username, "hash": hashed_pass, "salt": salt}
  # Next, we send the request to the API and put the response information into the variable 'r', json.dumps() function transforms the params
  # into JSON compatible
  r = requests.post(API, json.dumps(params))
  # Finally, the status code is returned by the function, it should be 200. We have to add error handling here for cases like the username
  # is already taken
  return {r.status_code}

def verifyUser ( password, username ):
  # First, we have to get the salt from the database so we can hash the password that the user is using to login. It would be much easier
  # to send the plain text password to the lambda function and let the process be taken care of there but it is unsecure to send plaintext
  # passwords through the network. We will have to take a look at this because it seems unefficent.
  # Here we specify the API url, in this case we are accessing the "salt" resource in the API
  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/salt"
  # We set our parameters, we only need the username for this one since we will just be searching the database for the salt
  params = {"username": username}
  # We prepare the request to be sent and make the request
  r = requests.post(API, json.dumps(params))
  
  # Using the salt that we just got from the database we will hash the password and send it to the API to confirm that the hash on the
  # database and the one we sent match
  hashed_pass = hashlib.sha512(password.encode('utf-8') + r.json()['body'].replace('"', '').encode('utf-8')).hexdigest()

  # We specify the "verifyuser" resource here to make our POST request
  API = "https://l11k4u8pyc.execute-api.us-east-2.amazonaws.com/Dev/verifyuser"
  # We prepare the params again, this time including the hashed password we want to send
  params = {"username": username, "password": hashed_pass}
  # Here we send the request and save the response in r
  r = requests.post(API, json.dumps(params))
  # The lambda function is built to return a True if the hashes match and a False if they don't, we return that boolean value here.
  # In the future, we can instead rely on the HTTP status code to know if the match succeeded or failed.
  return r.json()['body']
