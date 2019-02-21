from flask_bcrypt import Bcrypt

# Create the Hasher
bcrypt = Bcrypt()

def hash_pass(password):
    return bcrypt.generate_password_hash(password)

def check_pass(hashed_pass,password):
    return bcrypt.check_password_hash(hashed_pass, password)