import hashlib, uuid

# This function is for hashing and salting the passwords of our users
def createHash ( password ):
  # First, we create a randomly generated salt to be used in the hashing process
  salt = uuid.uuid4().hex
  # Next, we encode both the password and the salt as utf-8 before we combine them together and create their hash
  hashed_pass = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
  # Finally, the salt that we used and the hash are both returned so that we can store them in the User table.
  return {'hash':hashed_pass, 'salt':salt}

# This function helps us determine if the hash of the password that the user has entered is identical to the hash that we have store in our database
def verifyPass ( password, results ):
  # The results variable that we have as an argument in this function is actually a 2D list. The first item of the list (results[0][0])
  # is the hash and the second item (results[0][1]) is the salt. So, we make a hash using the password supplied by the user and the salt
  # that we kept from the user's registration process and then compare this hash with the one that we have stored in the database for the
  # user
  hashed_pass = hashlib.sha512(password.encode('utf-8') + results[0][1].encode('utf-8')).hexdigest()
  # If the hash that we have created is identical to the one in the database, then we pass true else false.
  if hashed_pass == results[0][0]:
    return True
  else:
    return False
