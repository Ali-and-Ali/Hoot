import hashlib, uuid

def createHash ( password ):
  salt = uuid.uuid4().hex
  hashed_pass = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
  return {'hash':hashed_pass, 'salt':salt}

def verifyPass ( password, results ):
  hashed_pass = hashlib.sha512(password.encode('utf-8') + results[0][1].encode('utf-8')).hexdigest()
  if hashed_pass == results[0][0]:
    return True
  else:
    return False
