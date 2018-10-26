import hashlib, uuid

def hashpass( password ):
  salt = uuid.uuid4().hex
  hash = hashlib.sha512(password + salt).hexdigest()
  return {'hash':hash, 'salt':salt}

def verifypass ( password, salt ):
  hash = hashlib.sha512(password + salt).hexdigest()
  return hash
