import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)  # Generate a 16-byte random salt
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + ":" + hashed_password  # Store salt & hash together

password1 = "password123"
password2 = "password123"

hashed1 = hash_password(password1)
hashed2 = hash_password(password2)

print(hashed1)  # Different hash each time
print(hashed2)  # Even if passwords are same, hashes are different!
