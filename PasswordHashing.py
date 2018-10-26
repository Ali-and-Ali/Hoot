import hashlib, uuid

def hashpass( password ):
  salt = uuid.uuid4().hex
  hashed_password = hashlib.sha512(password + salt).hexdigest()
  return {'hash':hashed_password, 'salt':salt}
